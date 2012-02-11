#!/usr/bin/python

#std
import logging
import urllib
#gae
from google.appengine.api import taskqueue
from google.appengine.ext import db
#3rd
from BeautifulSoup import BeautifulSoup
import web
#local
from top import top
from challenges import challenges
from golfers import golfers

urls = (
    '/', 'index',
    '/top', 'top',
    '/challenges/(.*)', 'challenges',
    '/(.*)', 'golfers.golfers',
)

class index:
    def GET(self):
        return 'index'
    def POST(self):
        """Update all challenges"""
        raise web.seeother('/')

def main():
    web.application(urls, globals()).cgirun()

if __name__ == '__main__':
    main()

