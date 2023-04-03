from django.shortcuts import render, HttpResponse, redirect
from .models import department, employee, Student
from datetime import datetime
from django.http import JsonResponse
from .forms import StudentForm
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.db.models import Q


# from django.template import loader
# from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Hello, world  !")

    return render(request, 'home.html', {'name': 'sharath'})


def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])

    result = val1+val2

    # print(val2)
    return render(request, 'result.html', {'res': result})


def addUser(request):

    return render(request, 'register.html')


def emppage(request):

    firstname = request.session.get('fname')

    lastname = request.session.get('lname')

    loginuserdetails = {
        'fname': firstname,
        'lname': lastname

    }

    return render(request, 'index.html', {'loginuserdetails': loginuserdetails})


def emp(request):
    # return HttpResponse("Hello, world  !")

    return render(request, 'register.html')

    # return render(request, 'index.html')


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
            return redirect('emppage')

        return render(request, 'index.html')


def sendjson(request):
    data = [

        {'name': 'sharath', 'email': 'peter@example.org'},
        {'name': 'banu', 'email': 'banu@example.org'}

    ]

    fruits = ['apple', 'banana']
    vege = ['pumpkin', 'tomata']

    a23 = fruits.extend(vege)

    print(fruits.pop())

    return JsonResponse(data, safe=False)


def addEmployee(request):

    if request.method == 'POST':

        firstname = request.POST['fname']
        lastname = request.POST['lastname']
        dept = request.POST['dept']
        salary = request.POST['salary']
        age = request.POST['age']
        hiredate = request.POST['hiredate']
        price = request.POST['price']
        img = request.POST['empimg']

        emprecord = employee(
            firstname=firstname, lastname=lastname,  salary=salary, age=age, hiredate=datetime.now(), Image=img, price=price, dept_id=dept)
        emprecord.save()

        ID = emprecord.id

        print('record employee insert', ID)

        return HttpResponse("yes emp data is", ID)

    else:

        Deptecords = department.objects.all()

        return render(request, 'addemp.html', {'dempdetails': Deptecords})


def viewEmployee(request):

    Employeerecords = employee.objects.all()

    listofemp = [Employeerecords]

    print(listofemp)

    return render(request, 'viewemp.html', {'empdetails': Employeerecords})


def indexform(request):
    student = StudentForm()
    return render(request, "student.html", {'form': student})


def logoutuser(request):

    del request.session['fname']

    return redirect('emppage')

# # form data try:
#                 form.save()
#                 return HttpResponse("yes working")
#                 # return redirect('/')
#             except:
#                 pass


def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        request.session['fname'] = firstname
        request.session['lname'] = lastname
        # form.fields
        print(firstname)
        print(lastname)
        print(form.visible_fields)
        if form.is_valid():
            try:
                print("pooppp")

                studentlogin = Student.objects.filter(
                    Q(firstname=firstname) & Q(lastname=lastname))
                if (studentlogin):
                    return redirect('emppage')
                else:
                    print("not valid")
                    return HttpResponse("not valid")

                # return HttpResponse(studentlogin)
                form.save()
                # return HttpResponse("File uploaded successfuly")

            except Exception as e:
                return HttpResponse(e)
                pass

    return HttpResponse("not curreent path")
    # return render(request, 'student.html', {'form': form})


def editEmployee(request):

    EMPiddd = request.GET['query']

    EmployeerecordsData = employee.objects.get(id=EMPiddd)

    EmployeerecordsData2 = employee.objects.values_list('Image')

    Employeerecords = employee.objects.values_list('Image')

    listofemp = [EmployeerecordsData]
    print(EmployeerecordsData)

    print(EmployeerecordsData2)

    context = {
        'oneempdata': EmployeerecordsData
    }

    return render(request, 'editemp.html', context)


def UPDATE(request, id):

    if request.method == 'POST':

        # EMPiddd = request.POST['empid']

        # print(EMPiddd)

        firstname = request.POST['fname']
        lastname = request.POST['lastname']
        dept = request.POST['dept']
        salary = request.POST['salary']
        age = request.POST['age']
        hiredate = request.POST['hiredate']
        price = request.POST['price']

        emprecord = employee(
            id=id, firstname=firstname, lastname=lastname,  salary=salary, age=age, hiredate=datetime.now(),  price=price, dept_id=1)
        emprecord.save()

        # return render(request, ' viewemp.html')

        # EmployeerecordsData.firstname = firstname
        # EmployeerecordsData.lastname = lastname
        # EmployeerecordsData.salary = salary
        # EmployeerecordsData.age = age
        # EmployeerecordsData.price = price

        # EmployeerecordsData.save()

        # print('record employee updated')

        # return HttpResponse("PLEASE update   EMPLOYEE ! ", empId)

        return redirect('viewEmployee')


def rememp(request, emp_id=0):

    if emp_id:
        try:
            emp_to_remove = employee.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse("EMPLOYEE  REMOVED SUCCESSFULLY  !")
        except:
            return HttpResponse("PLEASE ENTER VALID EMPLOYEE !")

    Employeerecords = employee.objects.all()

    context = {
        'emp': Employeerecords
    }

    return render(request, 'removeemp.html', context)


def filter(request):
    Departmentrecords = department.objects.all()

    context = {
        'emp': Departmentrecords
    }

    if request.method == 'POST':

        firstname = request.POST['fname']
        lastname = request.POST['lastname']
        dept = request.POST['dept']

        Employeerecords = employee.objects.all()

        if firstname != '':
            Employeerecords = Employeerecords.filter(
                Q(firstname=firstname) | Q(lastname=lastname))

        context2 = {
            'empdetails': Employeerecords
        }

        return render(request, 'viewemp.html', context2)

    elif request.method == '':

        return HttpResponse("please submit details for , filter  !")
    else:
        return render(request, 'filteremp.html', context)

    # return HttpResponse("add , filter  !")

 #    template = loader.get_template('home.html')

# context = {
 #   'fruits': ['Apple', 'Banana', 'Cherry'],
    # }

 # return HttpResponse(template.render(context, request))

# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
# template = loader.get_template('home.html')
# context = {
#    'fruits': ['Apple', 'Banana', 'Cherry'],
#  }
#  return HttpResponse(template.render(context, request))
