#!/usr/bin/python
# Get a list of challenges, and then store them to db.

import logging
import urllib
from google.appengine.ext import db
from BeautifulSoup import BeautifulSoup
import re
from obj_definition import *

re_entries      = re.compile(r'challenges/([0-9a-z]+)">(.*?)</a> - (\d+) entries')

def fetch(path):
    """Returns HTML string from vimgolf.com"""

    url = 'http://vimgolf.com/'+path
    logging.info('fetching '+url)
    return urllib.urlopen(url).read()

def update_db(tree):
    challenges = tree.findAll('h5')
    for c in challenges:
        result = re_entries.search(str(c))
        if result == None:
            continue
        record = Challenge()
        record.handle    = result.group(1)
        record.title     = result.group(2)
        record.entry_num = int(result.group(3))
        record.active_golfer_num = -1
        record.put()

if __name__ == "__main__":
    html = fetch('')    # root page gives us all challenges
    tree = BeautifulSoup(html)
    update_db(tree)
