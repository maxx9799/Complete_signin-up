from django import http
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)

from django.http import HttpResponse
from .forms import *
from .models import *
from django.views import View

# Create your views here.

def index(request):
    return render(request,"index.html")
    # Rendering a HTML page
def home(request):
    return HttpResponse("This is my users home page!!!!!!!!")
 
def signin(request):
    f = Login()
    return render(request, "signin.html", {'form':f})
    # we need to pass the form(class) contain in jinja through dict("keys":values) 

# def afterlogin(request):
#     form = Login(request.POST)
#     if form.is_valid(): #validating form data 
#         email = form.cleaned_data["email"]
#         password = form.cleaned_data["password"]
#         return HttpResponse(f"{email} {password}")

#     else:
#         error = "Invalid Response form"
#         form = Login()
#         return render(request, "signin.html", {'error':error})

def register(request):
    form = Signup()
    return render(request, "signup.html", {"form":form})

class aftersignup(View):
    def get(self, request):
        form = Signup()
        return render(request, "signup.html", {'form':form})

    def post(self, request):   #for post mtd req
        form = Signup(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"] 
            try:
                Adduser.objects.get(email=email)
            except:
                Adduser.objects.create(username=username, email=email, password=password, address=address)
                form = Login()
                return render(request, "signin.html", {'form':form})
            else:
                error = "Email Already Exists"
                form = Signup()
                return render(request, "Signup.html", {'form':form, 'error':error})


        else:
            error = "invalid form"
            form = Signup()
            return render(request, "Signup.html", {'form':form, 'error':error})

class aftersignin(View):
    def get(self, request):
        if request.session.get("email"):
            return render(request, "afterlogin.html")

        else:
            error = "No such methods are allowed"
            form = Login()
            return render(request, "signin.html", {'form':form, 'error':error})
            
    def post(self, request):
        form = Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                obj = Adduser.objects.get(email=email)
            except:
                error = "No such user"
                form = Login()
                return render(request, "signin.html", {'form':form, 'error':error})

            else:
                if obj.password == password:
                    request.session['email'] = email
                    request.session['islogin'] = 'true'
                    request.session.set_expiry(300)
                    return render(request, "afterlogin.html")
                    #return HttpResponse("Welcome.............")
                else:
                    error = "Incorrect Passsword"
                    form = Login()
                    return render(request, "signin.html", {'form': form, 'error':error})


def details(request):
    obj1 = Adduser.objects.all()
    return render(request, "details.html", {'data' : obj1})


def delete(request, id):

 
    obj2 = get_object_or_404(Adduser, id = id)
    print(obj2)
    if request.method =="GET":
        obj2.delete()
        test = f"Users email: {obj2} deleted"
        return render(request, 'delete.html', {'test':test})
    
    return render(request, "index.html")

def edit(request, id):
    obj3 = get_object_or_404(Adduser, id = id)
    if request.method == "GET":
        form = Signup(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'edit.html', {'form':form})
    
        # add form dictionary to context
        
        error = "Something Wrong"
        return render(request, 'index.html', {'error':error})


def logout(request):
    del request.session['email']
    del request.session['islogin']
    form = Login()
    return render(request, "signin.html", {'form': form})





