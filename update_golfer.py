#!/usr/bin/python
# Get stats of the specified golfer, calculate his total rank,
# and update the db.
# Request parameter: handle/id of the golfer

import logging
import urllib
import re
from BeautifulSoup import BeautifulSoup
from obj_definition import *
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

re_entries = re.compile(r'challenges/([0-9a-z]+)')

class UpdateGolfer(webapp.RequestHandler):
    def get(self):
        handle = self.request.get('handle')
        if handle == '':
            self.response.out.write('Need handle')
            return
        update_global_rank(handle)

def fetch(path):
    """Returns HTML string from vimgolf.com"""

    url = 'http://vimgolf.com/'+path
    logging.info('fetching '+url)
    return urllib.urlopen(url).read()

def update_global_rank(handle):
    """Returns global rank for golfer with handle."""

    challenges = Challenge.all()
    active_golfers = dict()
    for c in challenges:
        active_golfers[c.handle] = c.active_golfer_num

    html = fetch(handle)
    soup = BeautifulSoup(html)
    rows = soup.findAll('h5')
    g_rank = 0
    for r in rows:
        result = re_entries.search(str(r.a))
        if result==None:
            continue
        if r.b: # skip contributed challenges
            c_rank, entries = map(int, r.b.text.split('/')) # e.g. 1/100
            g_rank += int(active_golfers[result.group(1)]) - c_rank
    logging.info('Total rank for %s = %d' % (handle, g_rank))

    golfer = Golfer.gql("where handle = '%s'" % handle).get()
    if golfer:
        golfer.g_rank = g_rank
        golfer.put()
        logging.info('Update g_rank for %s' % handle)

# Example from google. Why is application a global variable?
application = webapp.WSGIApplication(
                                     [('/update_golfer', UpdateGolfer)],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

