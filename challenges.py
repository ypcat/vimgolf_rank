#std
import logging
#3rd
from google.appengine.api import taskqueue
from BeautifulSoup import BeautifulSoup
import web
#local
from model import Challenge
from util import fetch
from util import increment

class challenges:
    def GET(self, handle=None):
        challenge = Challenge.get_by_key_name(str(handle))
        if not challenge:
            raise web.seeother('/')
        render = web.template.render('templates')
        return render.challenges(challenge)
    def POST(self, handle=None):
        if handle:
            update_challenge(handle)
        else:
            update_challenges()

def update_challenges():
    """Fetch challenge list from vimgolf and update datastore."""
    logging.info('update_challenges()')

    rows = BeautifulSoup(fetch('/')).findAll('h5')
    count = increment('challenge_tasks', len(rows))
    logging.info('init challenge_tasks = %d' % count)
    for row in rows:
        handle = row.a['href'].split('/')[-1]
        taskqueue.add(url='/challenges/'+handle)

def update_challenge(handle):
    """Fetch Leaderboard and active golfers of the specified challenge, and update datastore."""
    logging.info('update_challenge(%s)' % handle)

    soup = BeautifulSoup(fetch('challenges/' + handle))
    title = soup.findAll('h3')[1].text
    golfers = [row.text.split('@')[-1] for row in soup.findAll('h5')[-1].parent.findAll('h6')]
    record = Challenge(key_name=handle, handle=handle, title=title, active_golfers=golfers)
    record.put()
    logging.info('updated Challenge(%s, %s) with %d golfers' % (handle, title, len(golfers)))

    count = increment('challenge_tasks', -1)
    logging.info('challenge_tasks = %d' % count)
    if count == 0:
        taskqueue.add(url='/top')

