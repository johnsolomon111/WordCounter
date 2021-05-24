from app import *

@server.route('/', methods=["GET","POST"])
def index():
    return "Hello"

@server.route('/wordcount', methods=["GET"])
def wordcount():
    '''
        Word count endpoit
        json parameter:
            {
                word : "sample word",
                url : "sample url"
            }
    '''
    usr_input = request.json
    if checkUrl(usr_input['url']):
        results = getSiteTextCount(usr_input['url'],usr_input['word'])
        if results['status'] == 'ok':
            addCount(usr_input['word'], usr_input['url'],results['count'])
        return results
