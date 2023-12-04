from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from .models import Emp,Testimonial
from .forms import EmpForm, FeedbackForm, EmpForm

# Create your views here.

def employee_home(request):
    emps=Emp.objects.all()
    return render(request, "employee/home.html", {'emps':emps})
def add_employee(request):
    if request.method=="POST":
        #data fetch
        emp_name=request.POST.get('emp_name')
        emp_id= request.POST.get("emp_id")
        emp_phone= request.POST.get("emp_phone")
        emp_address= request.POST.get("emp_address")
        emp_working= request.POST.get("emp_working")
        emp_department= request.POST.get("emp_department")

        #Validate


        #create model object and set the data
        e=Emp()
        e.name= emp_name
        e.emp_id= emp_id
        e.phone= emp_phone
        e.address= emp_address
        e.department= emp_department
        if emp_working is None:
            e.working= False
        else:
            e.working= True

        #save the object
        e.save()
        #prepare msg
        print("data is comming.......")
        return redirect("/employee/home/")
    form= EmpForm()
    return render(request, "employee/add_employee.html", {'form':form})
    #return HttpResponse("Hey man i'm sanjay what is your name?")

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    print(emp_id)
    return redirect("/employee/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"employee/update_emp.html",{
        'emp':emp
        })

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get('emp_name')
        emp_id_temp= request.POST.get("emp_id")
        emp_phone= request.POST.get("emp_phone")
        emp_address= request.POST.get("emp_address")
        emp_working= request.POST.get("emp_working")
        emp_department= request.POST.get("emp_department")
        e= Emp.objects.get(pk=emp_id)
        e.name= emp_name
        e.emp_id= emp_id_temp
        e.phone= emp_phone
        e.address= emp_address
        e.department= emp_department
        if emp_working is None:
            e.working= False
        else:
            e.working= True

        e.save()
    return redirect("/employee/home/")

