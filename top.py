import logging
import web
import datetime
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

def calc_rank(glist):
    for i in range(len(glist)):
        rank = i+1
        if i==0:
            glist[i].rank = rank
        elif glist[i-1].global_rank == glist[i].global_rank:
            glist[i].rank = glist[i-1].rank
        else:
            glist[i].rank = rank
    return glist

class top:
    def GET(self):
        glist = memcache.get('glist')
        if glist is None:
            glist = Golfer.all().order('global_rank')
            memcache.set("glist", glist);
        glist = calc_rank(list(glist))
        render = web.template.render('templates')
        return render.global_ranks(glist, str(datetime.datetime.utcnow()))
    def POST(self):
        """Update Golfer table from Challenge data."""
        logging.info('top()')
        challenges = list(Challenge.all())
        logging.info('gathering active golfers')
        handles = set(h for c in challenges for h in c.active_golfers)
        ranksum = sum(len(c.active_golfers) for c in challenges)
        golfers = dict((h, Golfer(key_name='@'+h, handle=h, global_rank=ranksum))
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

