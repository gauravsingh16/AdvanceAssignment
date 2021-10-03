import urllib.error
import urllib.request

def test_link():
    url = input('Enter a URL: ' )
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
