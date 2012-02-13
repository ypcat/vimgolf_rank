#std
import logging
#gae
from google.appengine.api import taskqueue
#3rd
from BeautifulSoup import BeautifulSoup
import web
#local
from top import top
from challenges import challenges
from golfers import golfers
from feed import feed
from model import Challenge

urls = (
    '/?', 'index',
    '/top/?', 'top',
    '/challenges/?', 'challenges',
    '/challenges/(.*)', 'challenges',
    '/json/(.*)', 'feed',
    '/(.*)', 'golfers.golfers',
)

class index:
    def GET(self):
        clist = sorted(Challenge.all(),
                       key=lambda c: len(c.active_golfers),
                       reverse=1)
        render = web.template.render('templates')
        return render.index(clist)
    def POST(self):
        """Update all challenges"""
        taskqueue.add(url='/challenges')
        raise web.seeother('/')

def main():
    web.application(urls, globals()).cgirun()

if __name__ == '__main__':
    main()

