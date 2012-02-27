#std
from datetime import datetime
#gae
from google.appengine.api import taskqueue, mail
#3rd
import web
#local
from top import top

class cron_challenges:
    def GET(self):
        """Update all challenges"""
        taskqueue.add(url='/challenges')

class cron_mail:
    def GET(self):
        toprankings = top()
        mailbody = str(toprankings.GET())
        mail.send_mail(sender="jyunfan@gmail.com",
                       to="jyunfan.vimgolf@blogger.com",
                       subject="Vimgolf rankings: " + str(datetime.utcnow()) + " UTC",
                       body=mailbody.encode('utf-8'))
