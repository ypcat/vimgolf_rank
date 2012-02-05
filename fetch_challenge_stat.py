#!/usr/bin/python
# Read html source of vimgold.com from stdin and collect information of each challenges.
# Craw overall challenge stat or specific user stat.
# Info includes challenge ID, number of entries, and challenge title.
# Feb 5 2012, Jyun-Fan Tsai

from StringIO import StringIO
#from lxml import etree
from BeautifulSoup import BeautifulSoup
import re
import sys

re_challenge_id = re.compile(r'/challenges/(.*)')
re_entries      = re.compile(r'(.*?) - (\d+) entries')
re_user_stat    = re.compile(r'Rank:\D+(\d+)/(\d+)');

def parse_overall(tree):
    #result = etree.tostring(tree.getroot(),
    #        pretty_print=True, method="html")
    #challenges = tree.xpath("//h5[@class='challenge']/a")
    challenges = tree.findAll('h5')
    for c in challenges:
        #result_challenge_id = re_challenge_id.search(c.attrib['href'])
        result_challenge_id = re_challenge_id.search(c.a['href'])
        if result_challenge_id == None:
            continue
        #result_entry = re_entries.search(etree.tostring(c, method='text'))
        result_entry = re_entries.search(str(c))
        if result_entry == None:
            continue
        print result_challenge_id.group(1) + "," + result_entry.group(2) + "," + result_entry.group(1)

def parse_user(tree):
    #result = etree.tostring(tree.getroot(),
    #        pretty_print=True, method="html")
    #challenges = tree.xpath("//h5[@class='challenge']/a")
    challenges = tree.findAll('h5')
    for c in challenges:
        #result_challenge_id = re_challenge_id.search(c.attrib['href'])
        result_challenge_id = re_challenge_id.search(c.a['href'])
        if result_challenge_id == None:
            continue
        #result_user_stat = re_user_stat.search(etree.tostring(c.getparent(), method='text'))
        result_user_stat = re_user_stat.search(str(c))
        if result_user_stat == None:
            continue
        print result_challenge_id.group(1) + "," + result_user_stat.group(1)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "Usage: fetch_challenge_stat.py [overall|user]"
        sys.exit(1)

    html   = sys.stdin.read()
    #parser = etree.HTMLParser()     # reference: http://lxml.de/parsing.html
    #tree   = etree.parse(StringIO(html), parser)
    tree = BeautifulSoup(html)

    if sys.argv[1]=='overall':
        parse_overall(tree)
    else:
        parse_user(tree)

