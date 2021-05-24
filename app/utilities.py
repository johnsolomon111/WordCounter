import bs4
import urllib.request
import requests
from pprint import pprint
def getSiteTextCount(url, word):
    '''
        Gets the whole page of the site using BS4
        get all the text on the given page
        return count
    '''
    try:
        source = urllib.request.urlopen(url).read()
        soup = bs4.BeautifulSoup(source,"html.parser")
        page = soup.find('body').getText()
        to_return = {
            'status' : 'ok',
            'count' : textCounter(word,page)
        }
        return to_return
    except Exception as e:
        print(e)
        to_return = {
            'status' : 'fail',
            'msg' : 'could not parse the page'
        }
        return to_return
    

def textCounter(word, page):
    '''
        Split the page text with spaces
        Append to a list if all the matching words
        then count the resulting list
    '''
    mathed = []
    page = page.strip()
    print(page)
    strings = page.replace("\t", " ").replace("\n", "").split(" ")
    pprint(strings)
    for string in strings:
        if string == word:
            mathed.append(string)
    return len(mathed)

def checkUrl(url):
    '''
        Check url validity using python requests
    '''
    req = requests.get(url)
    if req.status_code == 200:
        return True
    else:
        return False