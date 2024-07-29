from app import app
from flask import request
import yaml

@app.errorhandler(404)
def page_not_found(e):
    return f'Info not found, try again.\n', 404

@app.route('/')
def home():
    return "hey! this is a temporary web app for interacting with stuff, might integrate it into a storage server or something.\n"

@app.route('/api/<tool>', methods=['GET','POST'])
def api(tool):
   if tool == 'search':
       arg = request.args
       item = arg.get('item')
       de = yaml.unsafe_load(item)
       return de
   return f'{tool}'
#note: unfinished code, will do later...   
