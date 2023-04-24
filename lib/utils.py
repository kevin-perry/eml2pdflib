from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen


def can_url_fetch(src):
    try:
        req = Request(src)
        urlopen(req)
    except (HTTPError, URLError, ValueError):
        return False
    return True
