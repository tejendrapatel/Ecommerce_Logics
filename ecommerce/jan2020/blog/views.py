from django.shortcuts import render
from blog.models import *
from django.http import *
def firstpage(request):
    data = college.objects.all()
    d = {"college":data}
    return render(request,'home.html',d)
def secondpage(request):
    data = contact.objects.all()
    d = {"contact":data}
    return render(request,'contact.html',d)
def Details(request,c_id):
    data = contact.objects.get(id = c_id)
    d = {
        "stu":data
    }
    return render(request,'details.html',d)
    return HttpResponse("I want DEtails About ID: " + str(v1))
def detail(request,v1,v2,v3):
    a = 0
    if v3.lower() =="add":
        a = v1 + v2
    elif v3.lower() =="sub":
        a = v1 - v2
    elif v3.lower()=="mul":
        a =  v1 * v2
    elif v3.lower()=="div":
        a = v1 / v2
    else:
        a = "you  entered wrong option"
    return HttpResponse("your answer is : " + str(a))




def add_student(request):
    a =0
    if request.method =="POST":
        V1 = request.POST["v1"]
        V2 = request.POST["v2"]
        a = int(V1) + int(V2)
        a = int(V1) * int(V2)
        a = int(V1) / int(V2)
        a = int(V1) - int(V2)
    d = {
        'out': a
    }
    return  render(request, "add_student.html",d)
