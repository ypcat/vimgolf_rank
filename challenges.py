import web

class challenges:
    def GET(self, name):
        return 'challenges', name

app = web.application(('/(.*)', 'challenges'), globals())

