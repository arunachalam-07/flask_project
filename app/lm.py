from flask import *
from . import db_connect
from app import app
from app import *
from cryptography.fernet import Fernet as f
import uuid as uid
@app.route('/lm')
def lmpage():
    return render_template('lm.html',data=[{'name':'civil'},{'name':'cyber'},{'name':'land'}])
@app.route('/lm',methods=['POST'])

def lms():
    uname=request.form['user']
    passkey=request.form['pass']
    email=request.form['email']
    expert=request.form['expert']
    encoded_pass=cipher_suite.encrypt(bytes(passkey,'UTF-8'))
    decrpyt_pass=cipher_suite.decrypt(encoded_pass).decode('UTF-8')
    id=uid.uuid4()
    db_connect.db()
    g_name=uid.uuid4().hex
    sql="insert into lm(name,email,passkey,m_num,expert,t_id,g_u_name)"

