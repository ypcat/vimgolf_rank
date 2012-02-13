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

    # XXX limit to process first 5 items for testing
    #     take out the [:5] in the next line before deploy
    rows = BeautifulSoup(fetch('/')).findAll('h5')[:5]
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

#def update_challenge(handle):
#    """fetch Leaderboard and active golfers of the specified challenge, and update datastore."""
#    logging.info('update_challenge:' + handle)
#    html = fetch('challenges/' + handle)
#    tree = BeautifulSoup(html)
#    active_golfer_num = int(tree.find('b', { "class" : "stat" }).string)
#    print active_golfer_num
#    record = Challenge.get_by_key_name(handle)
#    if record == None:
#        return
#    record.active_golfers = active_golfer_num
#    record.put()
#
#    # Get games of all participated users
#    # example: '#5- Jaime A. S\xe1nchez /@jashbeta'
#    games = []
#    re_template = re.compile('#(\d+).*?@(\w+)$');
#    rows = tree.findAll('h6')
#    for r in rows:
#        if not r.a:
#            continue
#        result = re_template.search(r.text)
#        if result == None:
#            continue
#        [rank, user] = [result.group(1), result.group(2)]
#        g = Game(key_name=handle+':'+user)
#        g.challenge = handle
#        g.golfer = user
#        g.rank = int(rank)
#        games.append(g)
#    
#    # put
#    if len(games) > 0:
#        db.put(games)

