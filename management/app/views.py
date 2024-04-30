from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['un']
        password = request.POST['pass']
        # Attempt to find a user matching the provided credentials
        user = Login_data.objects.filter(username=username, password=password).first()
        # Check if a user was found
        if user:
            # If a matching user is found, render the home page
            return render(request, 'home.html')
        else:
            # If no matching user is found, redirect to signup
            return redirect('signup')
    else:
        # If the request method is not POST, render the login page again
        return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')



def about(request):
    return render(request,'about.html')

def signup(request):
    if request.method == "POST":
        name=request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        Login_data.objects.create(name=name,username=username, password=password)
        return redirect('login')
    return render(request, 'signup.html')

def sell(request):
    return render(request,'sell.html')

def buy(request):
    return render(request,'buy.html')

def base(request):
    return render(request,'base.html')

def property1(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Buyers_data.objects.create(name=name, email=email, phone=phone)
        return redirect('buy')
    return render(request,'property1.html')

def property2(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Buyers_data.objects.create(name=name, email=email, phone=phone)
        return redirect('buy')

    return render(request,'property2.html')

def property3(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Buyers_data.objects.create(name=name, email=email, phone=phone)
        return redirect('buy')
    return render(request,'property3.html')

def property4(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Buyers_data.objects.create(name=name, email=email, phone=phone)
        return redirect('buy')
    return render(request,'property4.html')

def buyers(request):
    buyers = Buyers_data.objects.all()
    return render(request, 'buyers.html', {'buyers': buyers})







