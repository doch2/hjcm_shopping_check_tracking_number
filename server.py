from flask import Flask, request, render_template
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random


app = Flask(__name__)
CORS(app)

cred = credentials.Certificate('firebase-adminkey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://hjcm-shopping-default-rtdb.asia-southeast1.firebasedatabase.app'
})



@app.route("/")
def searchPage():
    lotto_li = list(range(1,46))
    lotto = sorted(random.sample(lotto_li, 6))
    return render_template("search-number.html", variable=lotto)

@app.route("/result")
def resultPage():
    phoneNum = request.args.get('phoneNum')

    ref = db.reference('trackingNumberList')
    
    dbReference = (ref.get(phoneNum))[0]
    dbInfo = dbReference[phoneNum]
    
    handOverInfo = [dbInfo['name'], dbInfo['trackingNum']]

    return render_template("result.html", variable=handOverInfo)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)