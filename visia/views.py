from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from .models import Service, Contact
import random as r

# Create your views here.


def home(request):
    # return HttpResponse("Hello, world  visiaaaa !")

    Technology = Service.objects.all()

    serv1 = Service()
    serv1.name = 'python'

    serv2 = Service()
    serv2.name = 'salesforce'

    Technology = [serv1, serv2]

    return render(request, 'base.html',  {'dest1': Technology})


def contact(request):

    return HttpResponse("Hello, world  contact !")


def about(request):

    return HttpResponse("Hello, world 2222 about !")


def addUser(request):

    return render(request, 'register.html')


def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if User.objects.filter(username=username).exists():
            print('username already taken')
        elif User.objects.filter(email=email).exists():
            print('email already taken')
        else:
            userrecord = User.objects.create_user(
                username=username, first_name=firstname, last_name=lastname,   password=password, email=email)
            userrecord.save()
            print('user created')

        return render(request, 'register.html')


def login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'base.html', {'userdetails': user})

        else:
            print("invalid characters")

    else:

        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'base.html')


def contact(request):

    if request.method == 'POST':

        firstname = request.POST['firstname']
        email = request.POST['email']
        address = request.POST['address']
        qualifications = request.POST['qualifications']
        experience = request.POST['experience']

        Contactusers = Contact(Name=firstname, EmailID=email, Address=address,
                               Qualification=qualifications, Experience=experience)
        Contactusers.save()
        print("contact saved")

        return HttpResponse("contact record is inserted please check in admin side or your backend database !")

    # return render(request, 'base.html')


def otpGenerate(request):

    randomotp = ""

    val1 = int(request.POST["otp"])

    for i in range(0, 4):

        randomotp += str(r.randint(1, 9))

        print(" your one time password is "+randomotp)

        # return render(request,'result.html',{'otpresult':randomotp})
