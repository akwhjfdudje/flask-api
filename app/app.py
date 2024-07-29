from flask import Flask, request
from werkzeug.exceptions import HTTPException
import json
import pymongo
app = Flask(__name__)
dbclient = pymongo.MongoClient("mongodb://localhost:56735")
#vars for debugging purposes
dblist = dbclient.list_database_names()
if "posts" not in dblist:
    print("no posts in db, exiting...")
    exit()



@app.errorhandler(HTTPException)
def page_not_found(e):
    response = e.get_response()
    response.data = json.dumps({
        "code":e.code,
        "name":e.name,
        "description":e.description,
        })
    response.content_type = "application/json"
    return response
#debugging purposes
@app.route('/secret/')
def debug():
    return dblist

@app.route('/')
def home():
    return "hey! this is a temporary web app for interacting with stuff, might integrate it into a storage server or something.\n"

'''
@app.route('/api/<tool>', methods=['GET','POST'])
def api(tool):
   if tool == 'search':
       item = request.args.get('item')
       entry = search(item)
       return entry
   return f'{tool}'
#note: unfinished code, will do later...   

def search(item):
   return f'{item}'

'''
if __name__ == '__main__':
    app.run(debug=True)
