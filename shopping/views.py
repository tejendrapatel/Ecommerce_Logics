from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from shopping.models import *
from django.contrib.auth.models import User
def LOGIN(request):
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['user']
        p = d['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = True
    d = {'error': error}
    return render(request, "login.html", d)
def LOGOUT(request):
    logout(request)
    return redirect('home')
def Signup(request):
    error = False
    error2 = False
    if request.method == "POST":
        d = request.POST
        u = d['user']
        p = d['pwd']
        c = d['cpwd']
        f = d['fname']
        l = d['lname']
        e = d['em']
        user = User.objects.filter(username=u)
        if user:
            error2 = True
        elif c!=p:
            error = True
        else:
             User.objects.create_user(username=u, password=p,email= e,first_name =f,last_name =l)
             return redirect('Login')
    dd = {'error':error,'error2':error2}
    return render(request, "signup.html",dd)
def Forgot(request):
    error = False
    form = False
    udata = False
    if request.method == "POST":
        dd = request.POST
        name = dd["form"]
        if name == "submit email":
            e = dd['em']
            user = User.objects.filter(email = e)
            if user:
                form = True
                udata = user[0]
            else:
                error = True
        if name == 'submit pwd':
            p = dd ['pwd']
            c = dd ['cpwd']
            u = dd ['idd']
            user = User.objects.get(id=u)
            user.set_password(p)
            user.save()
            return redirect ('Login')
    d = {"form":form,"error":error,"udata":udata}
    return render(request,'forgot.html',d)
def All_category():
    allcat = Category.objects.all()
    return allcat
def Home(request):
    d = {"allcat":All_category()}
    return render(request,'index.html',d)
def About(request):
    d = {"allcat": All_category()}
    return render(request,'about.html',d)
def Contact(request):
    d = {"allcat": All_category()}
    return render(request,'contact.html',d)
def Blog(request):
    d = {"allcat": All_category()}
    return render(request,'blog.html',d)
def Blog_single(request):
    d = {"allcat": All_category()}
    return render(request,'blog-single.html',d)

def Checkout(request):
    d = {"allcat": All_category()}
    return render(request,'checkout.html',d)
def Cart(request):
    d = {"allcat": All_category()}
    return render(request,'cart.html',d)
def Category_detail(request,cat_id):
    catdata = Category.objects.get(id=cat_id)
    subdata = Subcategory.objects.filter(category= catdata).first()
    pro = Product.objects.filter(subcategory= subdata)
    d = {"subdata":subdata,"pro":pro,"cat":catdata,"allcat": All_category()}
    return render(request,'shop.html',d)
def Sub_detail(request,sub_id):
    subdata = Subcategory.objects.get(id=sub_id)
    pro = Product.objects.filter(subcategory=subdata)
    d = {"subdata": subdata, "pro": pro, "allcat": All_category()}
    return render(request,'sub_detail.html',d)
def Product_single(request,pro_id):
    subdata = Subcategory.objects.get(id=pro_id)
    pro = Product.objects.filter(subcategory=subdata)
    d = {"subdata": subdata, "pro": pro, "allcat": All_category()}
    return render(request,'product-single.html',d)
