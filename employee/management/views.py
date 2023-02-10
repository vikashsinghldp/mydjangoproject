from django.shortcuts import render,redirect
from management.models import Company,Employee
from management.forms import CompanyForm,EmployeeForm
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    return render(request,'home.html')

def loginCheck(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/emp")
        else:
            messages.info(request,'invalid credentials')
            return redirect
    else:
        form=loginForm()
        return render(request,'registration/login.html')



def comp(request):
    if request.method == 'POST':
        form =CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form=CompanyForm()    
    return render(request,"index.html",{'form':form})
#to retrieve company details
def show(request):
    companies=Company.objects.all()
    return render(request,"show.html",{'companies':companies})
# to edit company
def edit(request,cName):
    company=Company.objects.get(cName=cName)
    return render(request,'edit.html',{'company':company})
# to update company
def update(request,cName):
    company=Company.objects.get(cName=cName)
    form=CompanyForm(request.POST,instance=company)
    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request,'edit.html',{'company':company})

#to delete company details
def delete(request,cName):
    company=request.objects.get(cName=cName)
    company.delete()
    return redirect('/show')

#To create employee
def emp(request):
    if request.method == 'POST':
        form =EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/showemp")
            except:
                pass
    else:
        form=EmployeeForm()    
    return render(request,"addemp.html",{'form':form})

def showemp(request):
    employees=Employee.objects.all()
    return render(request,"showemp.html",{'employees':employees})

def deleteEmp(request,eFname):
    employee=Employee.objects.get(eFname=eFname)
    employee.delete()
    return redirect("/showemp")

def editemp(request,eFname):
    employee=Employee.objects.get(eFname=eFname)
    return render(request,"editemployee.html",{'employee':employee})

#To update employee
def updateEmp(request,eFname):
    employee=Employee.objects.get(eFname=eFname)
    form =EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/showemp")
    return render(request,"editemployee.html",{'employee':employee})