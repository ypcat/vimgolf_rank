import logging
import urllib
from google.appengine.ext import db
from model import Counter

def fetch(path):
    """Returns file object from vimgolf.com"""

    path = path if path.startswith('/') else '/'+path
    url = 'http://vimgolf.com'+path
    logging.info('fetching '+url)
    return urllib.urlopen(url)

def increment(key_name, amount):
    """Increment counter atomically.

    key_name = counter name
    amount = increment amount, can be negative

    Returns counter after increment.
    """
    def txn(key_name, amount):
        counter = Counter.get_by_key_name(key_name)
        if not counter:
            counter = Counter(key_name=key_name, count=0)
        counter.count += amount
        counter.put()
        return counter.count
    return db.run_in_transaction(txn, key_name, amount)

