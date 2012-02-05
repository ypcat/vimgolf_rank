#!/usr/bin/python

import logging
import urllib
from google.appengine.api import taskqueue
from google.appengine.ext import db
from BeautifulSoup import BeautifulSoup
import web

urls = (
    '/', 'index',
    '/user', 'user',
    '/top', 'top',
)

class index:
    """URL handler for /"""

    def GET(self):
        golfers = top_golfers()
        for golfer in golfers:
            print '<div>%d %s %d</div>' % (golfer.rank, golfer.handle, golfer.g_rank)

class user:
    def POST(self):
        """Update user rank and store in database"""
        i = web.input()
        golfer = Golfer()
        golfer.handle = i.handle
        golfer.rank = int(i.rank)
        golfer.g_rank = global_rank(golfer.handle)
        golfer.put()

class top:
    def POST(self):
        """Update LeaderBaord and store in database"""
        html = fetch('top')
        soup = BeautifulSoup(html)
        rows = soup.findAll('h6')[1:] # skip first <h6>, not user record
        handles = [r.a.text[1:] for r in rows]

        leaderboard = LeaderBoard.gql('').get()
        if not leaderboard:
            leaderboard = LeaderBoard()
        leaderboard.handles = handles
        leaderboard.put()

class LeaderBoard(db.Model):
    """Top 100 user handles. This should have only one record."""
    handles = db.StringListProperty()

class Golfer(db.Model):
    """Data model for user"""

    handle = db.StringProperty()
    rank = db.IntegerProperty()
    g_rank = db.IntegerProperty()

def fetch(path):
    """Returns HTML string from vimgolf.com"""

    url = 'http://vimgolf.com/'+path
    logging.info('fetching '+url)
    return urllib.urlopen(url).read()

def global_rank(handle):
    """Returns global rank for golfer with handle."""

    html = fetch(handle)
    soup = BeautifulSoup(html)
    rows = soup.findAll('h5')
    g_rank = 0
    for r in rows:
        if r.b: # skip contributed challenges
            c_rank, entries = map(int, r.b.text.split('/')) # e.g. 1/100
            g_rank += entries - c_rank
    return g_rank

def top_golfers():
    """Returns top 100 Golfer."""

    leaderboard = LeaderBoard.gql('').get()
    if not leaderboard:
        taskqueue.add(url='/top')
        return []

    handles = leaderboard.handles
    golfers = []
    for i, handle in enumerate(handles):
        golfer = Golfer.gql("where handle = '%s'" % handle).get()
        if golfer:
            golfers.append(golfer)
        else:
            taskqueue.add(url='/user', params={'handle':handle, 'rank':i+1})

    return golfers

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.cgirun()

