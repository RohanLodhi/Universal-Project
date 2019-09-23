from django.shortcuts import render, redirect
from django.http import HttpResponse
import MySQLdb
# Create your views here.
def test(req):
    return render(req, 'adddata.html')

def getdata(req):
    studentID = req.GET.get('id')
    studentName = req.GET.get('Name')
    
    studentMbNumber = req.GET.get('MobileNumber')
    studentAddress = req.GET.get('Address')
    studentCourse = req.GET.get('Course')

    query = "insert into Students(id, Name, MobileNumber, Course, Address) values({0},'{1}',{2},'{3}','{4}')".format(studentID, studentName, studentMbNumber, studentAddress,studentCourse)
    con = MySQLdb.connect("localhost", "root", "root", "Students")
    cur = con.cursor()
    data = cur.execute(query)
    con.commit()
    return HttpResponse(data)
    #return render(req,'adddata.html')

def showdata(req):
    con = MySQLdb.connect("localhost", "root", "root", "Students")
    cur = con.cursor()
    query = "select * from Students"
    data = cur.execute(query)
    res = cur.fetchall()
    con.commit()
    return render(req, 'viewdata.html',{data:res})

