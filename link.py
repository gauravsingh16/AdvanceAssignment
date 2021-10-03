import urllib
<<<<<<< HEAD
import requests

def test_link(url):
=======
def test_link():
    url = input('Enter a URL: ')
>>>>>>> 5fe5943f684e597f57a238f2eb9c8cb436b21f4d
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
<<<<<<< HEAD

url = input('Enter a URL: ')
test_link(url)
=======
>>>>>>> 5fe5943f684e597f57a238f2eb9c8cb436b21f4d
