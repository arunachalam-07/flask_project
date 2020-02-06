from app import app 
import pymysql
myconn=pymysql.connect(host='localhost',user='root',password='',database='nodedb')
cur=myconn.cursor()