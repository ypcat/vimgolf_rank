from google.appengine.ext import db

class Challenge(db.Model):
    handle            = db.StringProperty()
    title             = db.StringProperty()
    active_golfer_num = db.IntegerProperty()
    entry_num         = db.IntegerProperty()


class Golfer(db.Model):
    handle = db.StringProperty()
    rank = db.IntegerProperty()
    g_rank = db.IntegerProperty()

