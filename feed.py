#std
import simplejson as json
#3rd
import web
#local
from model import Challenge
from model import Golfer

class feed:
    def GET(self, path=None):
        web.header('Content-Type', 'application/json')
        if path == 'top':
            return json_top()
        elif path == 'challenges':
            return json_challenges()
        else:
            return json.dumps(None) # null

def json_challenges():
    return json.dumps(dict(
        (c.handle, {
            'title':c.title,
            'active_golfers':len(c.active_golfers),
        }) for c in Challenge.all()))

def json_top():
    return json.dumps(dict(
        (g.handle, {
            'rank':g.rank,
            'global_rank':g.global_rank,
        }) for g in Golfer.all()))

