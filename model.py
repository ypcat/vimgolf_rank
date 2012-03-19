from google.appengine.ext import db

class Challenge(db.Model):
    handle         = db.StringProperty(indexed=False)     # challenge id, 24 letters
    title          = db.StringProperty(indexed=False)
    active_golfers = db.StringListProperty(indexed=False) # list of golfer handles

class Golfer(db.Model):
    handle         = db.StringProperty(indexed=False)
    global_rank    = db.IntegerProperty(indexed=True)    # sum of ranks of all challenges

class Counter(db.Model):
    count          = db.IntegerProperty(indexed=False)

