from app import app 
import pymysql
from app import *
from app import usr_reg
def db():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='nodedb')
    cur=myconn.cursor()
