from google.appengine.ext import db

class Challenge(db.Model):
    handle         = db.StringProperty()    # challenge id, 24 letters
    title          = db.StringProperty()
    active_golfers = db.IntegerProperty()
    entries        = db.IntegerProperty()   # total number of submissions


class Golfer(db.Model):
    handle         = db.StringProperty()
    global_rank    = db.IntegerProperty()   # sum of ranks of all challenges
    rank           = db.IntegerProperty()

class Game(db.Model):
    """Data model for a game."""
    golfer = db.StringProperty()
    challenge = db.StringProperty()
    rank = db.IntegerProperty()
