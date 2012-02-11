from google.appengine.ext import db

class Challenge(db.Model):
    handle         = db.StringProperty()
    title          = db.StringProperty()
    active_golfers = db.IntegerProperty()
    entries        = db.IntegerProperty()


class Golfer(db.Model):
    handle         = db.StringProperty()
    global_rank    = db.IntegerProperty()

class Leaderbaord(db.Model):
    rank           = db.IntegerProperty()
    handle         = db.StringProperty()

