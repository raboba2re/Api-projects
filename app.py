from flask import Flask, json

from flask_cors import CORS

app = Flask('__name__')


@app.route('/') 
def assingment():
   
   work = { "name": "Rabo Bature",
           "username": "RBJ",
           "address": "Manchok",
           "Phone number": "08100561772", }
   return json.dumps(work)


if __name__ ==('__main__'):
    app.run(debug=True)

