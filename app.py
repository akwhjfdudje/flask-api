from flask import Flask, request, make_response, abort
from werkzeug.exceptions import HTTPException
import json
import pymongo
from random import randrange
from bson.json_util import dumps, loads

app = Flask(__name__)
dbclient = pymongo.MongoClient("mongodb://127.0.0.1:56735")
#vars for debugging purposes
dblist = dbclient.list_database_names()
if "posts" not in dblist:
    print("no database called posts, exiting...")
    exit()
posts_db = dbclient["posts"]

if "posts" not in posts_db.list_collection_names():
    print("no collections called posts in database posts, exiting...")
posts_col = posts_db["posts"]

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
    response = make_response(dumps({"message" : "hey! this is a temporary web app."}))
    response.content_type = "application/json"
    return response

@app.route('/api/posts/<path:option>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle(option):
   calls = {"random": random(), "all" : all_posts(), "create": create(request.get_data())}
   options = option.split("/")
   for i in options:
       if i in list(calls.keys()):
           return calls[i]
       else:
           abort(404)
   '''
   if options[0] == "" and request.method == "GET":
       if len(options) == 1:
           return all_posts()
       if options[1] == "":
           return all_posts()
       if options[0] == "random":
           return random()
   if options[0] == "create":
       return '', 204
   else:
       abort(404)
    '''
def all_posts():
    response = make_response(dumps(list(posts_col.find({}, {"_id":0}))))
    response.content_type = "application/json"
    return response

def random():
   pipeline = [{"$sample" : { "size" : 1}},{"$project" : {"_id": 0}}]
   post = list(posts_col.aggregate(pipeline))
   response = make_response(dumps(list(post)[0]))
   response.content_type = "application/json"
   return response

def create(data):
   return data


if __name__ == '__main__':
    app.run()
