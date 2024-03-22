from flask import Flask, request
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return f'Info not found, try again.\n', 404

@app.route('/')
def home():
    return "hey! this is a temporary web app for interacting with stuff, might integrate it into a storage server or something.\n"

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

if __name__ == '__main__':
    app.run(debug=True)
