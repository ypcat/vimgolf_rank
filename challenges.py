#std
import logging
import re
#3rd
from google.appengine.ext import db
from BeautifulSoup import BeautifulSoup
import web
#local
from model import Challenge, Game
from util import fetch

class challenges:
    def GET(self, name):
        return 'challenges', name
    def POST(self):
        i = web.input()
        update_challenge(i.handle)

def update_challenge(handle):
    """fetch Leaderboard and active golfers of the specified challenge, and update datastore."""
    logging.info('update_challenge:' + handle)
    html = fetch('challenges/' + handle)
    tree = BeautifulSoup(html)
    active_golfer_num = int(tree.find('b', { "class" : "stat" }).string)
    print active_golfer_num
    record = Challenge.get_by_key_name(handle)
    if record == None:
        return
    record.active_golfers = active_golfer_num
    record.put()

    # Get games of all participated users
    # example: '#5- Jaime A. S\xe1nchez /@jashbeta'
    games = []
    re_template = re.compile('#(\d+).*?@(\w+)$');
    rows = tree.findAll('h6')
    for r in rows:
        if not r.a:
            continue
        result = re_template.search(r.text)
        if result == None:
            continue
        [rank, user] = [result.group(1), result.group(2)]
        g = Game(key_name=handle+':'+user)
        g.challenge = handle
        g.golfer    = user
        g.rank      = int(rank)
        games.append(g)
    
    # put
    if len(games) > 0:
        db.put(games)

#app = web.application(('/(.*)', 'challenges'), globals()) # why this line?

