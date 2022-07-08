import requests

DEFAULT_ITEMS_URL = 'https://barotraumagame.com/wiki/Category:Items'


def get_webpage(url):
    """
    Get the webpage
    """
    response = requests.get(url)
    return response


if __name__ == '__main__':
    print("OK")