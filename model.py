from google.appengine.ext import db

class Challenge(db.Model):
    handle         = db.StringProperty()     # challenge id, 24 letters
    title          = db.StringProperty()
    active_golfers = db.StringListProperty() # list of golfer handles

class Golfer(db.Model):
    handle         = db.StringProperty()
    global_rank    = db.IntegerProperty()    # sum of ranks of all challenges
    rank           = db.IntegerProperty()

class Counter(db.Model):
    count          = db.IntegerProperty()

