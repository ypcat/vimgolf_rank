#!/usr/bin/python
# Get info of each challenge, and store them to db.

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

def update_challanges(tree):
    result = Challenge.all()
    for record in result:
        print 'challenges/'+record.handle
        c_html = fetch('challenges/'+record.handle)
        tree = BeautifulSoup(c_html)
        active_golfer_num = int(tree.find('b', { "class" : "stat" }).string)
        print active_golfer_num 
        record.active_golfer_num = active_golfer_num
        record.put()

if __name__ == "__main__":
    update_challanges(tree)
