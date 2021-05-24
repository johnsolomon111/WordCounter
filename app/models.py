from app import *

def createCountTable():
    '''
        Create DB and table to insert results
    '''
    conn = sqlite3.connect('wordcount.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE wordcounts (
        word TEXT,
        url TEXT,
        count INTEGER
    )""")
    conn.commit()
    conn.close()

def addCount(word,url,count):
    '''
        Insert to table the new results
    '''
    conn = sqlite3.connect('wordcount.db')
    cursor = conn.cursor()
    query = '''INSERT INTO wordcounts VALUES("{}","{}",{})'''.format(word,url,count)
    cursor.execute(query)
    conn.commit()
    conn.close()
    