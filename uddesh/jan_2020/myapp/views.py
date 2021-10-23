from django.http import HttpResponse
from django.shortcuts import render,redirect
from myapp.models import *
def homepage(request):
    return render(request,"home.html")
def studentpage(request):
    data=students.objects.all()
    dicto={"key1":data}
    return render(request,"students.html",dicto)
def detailspage(request,s_id):
    data1=students.objects.get(id=s_id)
    dicto={"key1":data1}
    return render(request,"details.html",dicto)
def teacherpage(request):
    data=teachers.objects.all()
    dicto={"key1":data}
    return render(request,"teachers.html",dicto)
def teacherdetails(request,t_id):
    data=teachers.objects.get(id=t_id)
    dicto={"key1":data}
    return render(request,"tdetails.html",dicto)
def userpage(request):
    return render(request,"user.html")
def loginpage(request):
    return render(request,"login.html")
def contactpage(request):
    return render(request,"contact.html")
def s_sign_up(request):
    allcolleges=college.objects.all()
    dd={"clgs":allcolleges}
    if request.method == "POST":
        d= request.POST
        n=d['sname']
        r=d['srnum']
        u=d['snum']
        e=d['semail']
        i=d['simage']
        c=d['cid']
        cdata=college.objects.get(id=c)
        students.objects.create(name=n,email=e,number=u,image=i,rollno=r,clg=cdata)
        return redirect("home")
    return render(request, "sign_up.html",dd)

def tsign_up(request):
    if request.method == "POST":
        d= request.POST
        n=d['tname']
        r=d['trnum']
        u=d['tnum']
        e=d['temail']
        teachers.objects.create(name=n,email=e,number=u,teacherid=r)
        return redirect("home")
    return render(request, "tsign_up.html")
def s_delete(request,s_id):
    data=students.objects.get(id=s_id)
    data.delete()
    return redirect('home')

def edit_student(request,s_id):
    data=students.objects.get(id=s_id)
    data2=college.objects.all()
    d={"details":data,"clgs":data2}
    return render(request,"s_edit.html",d)


def calci(request):
    a = 0
    if request.method == "POST":
        v1 = request.POST['v1']
        v2 = request.POST['v2']
        a = int(v1)+int(v2)
    d = {"out": a
        }
    return render(request, "calci.html", d)

