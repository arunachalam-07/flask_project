from app import app
from flask import make_response
import http.cookies
c=http.cookies.SimpleCookie()
c['my_cookie']='arun'
@app.route('/cookie')
def cookie():
    res=make_response('setting cookie');
    res.set_cookie('cookie1',c,10);
    return res