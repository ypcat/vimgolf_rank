#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib

soup = BeautifulSoup(open('top100.html').read())
for row in soup.findAll('h6')[1:]:
    user = row.a['href'][1:]
    print user
    f = open('top100/'+user,'w')
    f.write(urllib.urlopen('http://vimgolf.com/'+user).read())
    f.close()

