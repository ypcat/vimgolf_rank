import web

class top:
    def GET(self):
        return 'top'

app = web.application(('/?', 'top'), globals())

