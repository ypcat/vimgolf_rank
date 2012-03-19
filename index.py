#std
import logging
from datetime import datetime
#gae
from google.appengine.api import taskqueue, memcache
#3rd
from BeautifulSoup import BeautifulSoup
import web
import PyRSS2Gen
#local
from top import top
from challenges import challenges
from golfers import golfers
from feed import feed
from model import Challenge
from cron import cron_challenges, cron_mail

urls = (
    '/?', 'index',
    '/top/?', 'top',
    '/challenges/?', 'challenges',
    '/challenges/(.*)', 'challenges',
    '/json/(.*)', 'feed',
    '/cron/challenges', 'cron_challenges',
    '/cron/mail', 'cron_mail',
    '/rss', 'rss',
    '/(.*)', 'golfers.golfers',
)

class index:
    def GET(self):
        clist = memcache.get('clist')
        if clist is None:
            clist = sorted(Challenge.all(),
                       key=lambda c: len(c.active_golfers),
                       reverse=1)
            memcache.set("clist", clist);
        render = web.template.render('templates')
        return render.index(clist)
    def POST(self):
        """Update all challenges"""
        taskqueue.add(url='/challenges')
        raise web.seeother('/')

class rss:
    def GET(self):
        toprankings = top()
        html = str(toprankings.GET())
        rss = PyRSS2Gen.RSS2(
            title = 'Vimgolf rankings',
            description = 'RSS feed for newest Vimgolf rankings',
            link = 'http://vimgolf-rank.appspot.com',
            lastBuildDate = datetime.utcnow(),
            items = [
                PyRSS2Gen.RSSItem(
                    title = str(datetime.utcnow()),
                    description = html,
                    pubDate = datetime.utcnow(),
                    )
            ])
        return rss.to_xml(encoding='utf-8')

def main():
    web.application(urls, globals()).cgirun()

if __name__ == '__main__':
    main()

