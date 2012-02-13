import logging
import web

class top:
    def GET(self):
        return 'top'
    def POST(self):
        """Update Golfer table from Challenge data."""
        logging.info('top()')

