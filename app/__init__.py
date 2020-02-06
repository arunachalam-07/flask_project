from flask import *
app=Flask(__name__)

from app import views
from app import admin_views
from app import usr_reg
from app import cookie
from app import db_connect