import logging
import urllib

def fetch(path):
    """Returns file object from vimgolf.com"""

    path = path if path.startswith('/') else '/'+path
    url = 'http://vimgolf.com'+path
    logging.info('fetching '+url)
    return urllib.urlopen(url)

