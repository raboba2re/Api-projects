from flask import Flask, json

from flask_cors import CORS

app = Flask('__name__')


@app.route('/') 
def assingment():
   
   work = { "name": "Rabo Bature",
           "username": "RBJ",
           "address": "Manchok",
           "Phone number": +2348100561772,
           "email":"rabobature@gmail.com"}
   return json.dumps(work)


if __name__ ==('__main__'):
    app.run(debug=True)

