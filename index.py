#std
import logging
#import re
#gae
from google.appengine.api import taskqueue
#from google.appengine.ext import db
#3rd
from BeautifulSoup import BeautifulSoup
import web
#local
from util import fetch
from top import top
from challenges import challenges
from golfers import golfers
from model import Challenge

urls = (
    '/?', 'index',
    '/top/?', 'top',
    '/challenges/?', 'challenges',
    '/challenges/(.*)', 'challenges',
    '/(.*)', 'golfers.golfers',
)

class index:
    def GET(self):
        clist = sorted(Challenge.all(),
                       key=lambda c: len(c.active_golfers),
                       reverse=1)
        link = lambda c:'<a href="challenges/%s">%s</a>' % (c.handle, c.title)
        active = lambda c:'%d active golfers' % len(c.active_golfers)
        row = lambda c: '<div>%s - %s</div>' % (link(c), active(c))
        d = {'body':'\n'.join(row(c) for c in clist)}
        return '''
        <h3><b>Open VimGolf Challenges</b></h3>
        <h4><a href="/top">Leaderboard</a></h4>
        <div>
            %(body)s
        </div>''' % d
    def POST(self):
        """Update all challenges"""
        taskqueue.add(url='/challenges')
        raise web.seeother('/')

#def update_challenge_list():
#    """fetch challenge list from vimgolf and update datastore."""
#    logging.info('update_challenge_list')
#
#    re_entries = re.compile(r'challenges/([0-9a-z]+)">(.*?)</a> - (\d+) entries')
#
#    html = fetch('') # root page returns the list challenges
#    tree = BeautifulSoup(html)
#    challenges = tree.findAll('h5')
#    updated_challenges = []
#    for c in challenges:
#        result = re_entries.search(str(c))
#        if result == None:
#            continue
#        handle = result.group(1)
#        if Challenge.get_by_key_name(handle) != None:
#            logging.info('Skip challenge' + result.group(2))
#            continue
#        record = Challenge(key_name=handle)
#        record.handle = handle
#        record.title = result.group(2)
#        record.entries = int(result.group(3))
#        record.active_golfers = -1
#        updated_challenges.append(record)
#        logging.info('Add challenge ' + record.title)
#    if len(updated_challenges)>0:
#        db.put(updated_challenges)

def main():
    web.application(urls, globals()).cgirun()

if __name__ == '__main__':
    main()

