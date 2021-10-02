import urllib
import requests

def test_link(url):
    try:   
        result = urllib.request.urlopen(url,None,4).getcode()
        if result == 200:
            print('This link is live')
            return True
            
    except urllib.error.HTTPError as e:
        print('This link is dead')
        return False
    except urllib.error.URLError as e:
        return e

url = input('Enter a URL: ')
test_link(url)
