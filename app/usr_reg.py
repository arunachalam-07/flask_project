from flask import *
from app import app
from app import db_connect
from cryptography.fernet import Fernet as f

@app.route('/usr__reg')
def usr_reg():
    return render_template('usr_reg.html')
@app.route('/usr__reg',methods=['POST'])
def get_values():
    key=f.generate_key()
    cipher_suite=f(key)
   
    uname=request.form['user']
    passkey=request.form['pass']
    email=request.form['email']
    encoded_pass=cipher_suite.encrypt(bytes(passkey,'UTF-8'))
    decrpyt_pass=cipher_suite.decrypt(encoded_pass).decode('UTF-8')
    return jsonify(results=li)
    
    