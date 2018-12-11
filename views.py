from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    #database operation specific
    #create a connection to databases 
    #USER ,PASS,HOST ,DBNAME
    #uname=request.GET["user"]
    #passw=request.GET["pass"]
    uname=request.GET["user"]
    passw=request.GET["password"]
    import pymysql as pys
    conn=pys.connect(user="root",password="user",host="localhost",db="python")
    """connection will bring response in form of cursor"""
    cur=conn.cursor()
    #create a query ->insert
    query1="INSERT into login(user,password) values('"+uname+"','"+passw+"')"
    #execute query using cursor and recieve responses
    cur.execute(query1)
	
    #commit the executon
    conn.commit()
    #check no of rows added
    rc=cur.rowcount
    if rc>0:
        response="Signedup sucessfully"
    else:
        response="Signup failed"
    return HttpResponse(response)
def login(request):
    uname=request.GET["user"]
    passw=request.GET["password"]
    import pymysql as pys
    conn=pys.connect(user="root",password="user",host="localhost",db="python")
    """connection will bring response in form of cursor"""
    cur=conn.cursor()
    query1="select * from login where user='"+uname+"' and password='"+passw+"'"
    #execute query using cursor and recieve responses
    cur.execute(query1)
    #commit the executon
    conn.commit()
    #check no of rows added
    rc=cur.rowcount
    if rc>0:
        response="loggedin sucessfully"
    else:
        response="Invalid Credentials"
    return HttpResponse(response)
def predict(request):
    #recive hours studied
    hrs=int(request.GET["hours"])
    #implemenat ML
    import pandas as p
    df=p.read_csv("D:\project_django\data_set\Grade_Set_1.csv")
    import numpy
    import sklearn.linear_model as lm
    x=df.Hours_Studied[:,numpy.newaxis]
    y=df.Test_Grade[:,numpy.newaxis]
    lr=lm.LinearRegression()
    lr.fit(x,y)
    marks=lr.predict(hrs)
    marks=int(marks)
    resp="student who study for " +str(hrs)+ " hours will score "+str(marks)+" marks                                                                                                                                                                                                        1                   q"
    return HttpResponse(resp)