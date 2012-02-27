import logging
import web
#gae
from google.appengine.api import taskqueue, memcache
from google.appengine.ext import db
#local
from model import Challenge
from model import Golfer

def fix_keyname(name):
    if name.startswith('__'):
        name += '@'
    return name

class top:
    def GET(self):
        glist = memcache.get('glist')
        if glist is None:
            glist = Golfer.all().order('global_rank')
            memcache.set("glist", glist);
        render = web.template.render('templates')
        return render.global_ranks(glist)
    def POST(self):
        """Update Golfer table from Challenge data."""
        logging.info('top()')
        challenges = list(Challenge.all())
        logging.info('gathering active golfers')
        handles = set(h for c in challenges for h in c.active_golfers)
        ranksum = sum(len(c.active_golfers) for c in challenges)
        golfers = dict((h, Golfer(key_name=fix_keyname(h), handle=h, global_rank=ranksum))
                       for h in handles)
        logging.info('global rank sum %d' % ranksum)
        logging.info('calculating global rank for each golfer')
        for c in challenges:
            n = len(c.active_golfers)
            for i, h in enumerate(c.active_golfers):
                golfers[h].global_rank -= n - i - 1
        logging.info('calculating rank for each golfer')
        glist = golfers.values()
        db.put(glist)
        logging.info('done updating golfer ranking')

