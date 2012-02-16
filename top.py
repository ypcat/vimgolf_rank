import logging
import web
from model import Challenge
from model import Golfer

class top:
    def GET(self):
        return 'top'
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
        keyfunc = lambda g: g.global_rank
        for i, g in enumerate(sorted(golfers.values(), key=keyfunc)):
            g.rank = i + 1 # XXX what if 2 golfer have same global rank?
            g.put()
        logging.info('done updating golfer ranking')

