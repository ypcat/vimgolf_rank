#!/usr/bin/python

import logging
import urllib
from google.appengine.ext import db
from BeautifulSoup import BeautifulSoup

class Golfer(db.Model):
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

    query = Golfer.gql("where rank <= 100")
    if query.count() == 100:
        return list(query)

    golfers = []
    html = fetch('top')
    soup = BeautifulSoup(html)
    rows = soup.findAll('h6')[1:] # skip first <h6>, not user record
    for i, r in enumerate(rows):
        handle = r.a.text[1:] # skip '@' in @handle
        golfer = Golfer.gql("where handle = '%s'" % handle).get()
        logging.info('%d %s %s'%(i+1,handle,repr(golfer)))
        if not golfer:
            golfer = Golfer()
            golfer.handle = handle
            golfer.rank = i + 1
            golfer.g_rank = global_rank(golfer.handle)
            golfer.put()
        golfers.append(golfer)
    return golfers

print 'Content-Type: text/html\n'

golfers = top_golfers()
for golfer in golfers:
    print '<div>%d %s %d</div>' % (golfer.rank, golfer.handle, golfer.g_rank)

