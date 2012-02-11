import logging
import urllib

def fetch(path):
    """Returns HTML string from vimgolf.com"""

    url = 'http://vimgolf.com/'+path
    logging.info('fetching '+url)
    return urllib.urlopen(url).read()
