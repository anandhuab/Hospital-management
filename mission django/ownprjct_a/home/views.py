from django.shortcuts import render

# from ownprjct_a.home.forms import BookingForm
from . models import Department, Doctors

from. forms import BookingForm

# Create your views here.
def index(request):
    person = {
        'name': 'Anandhu A B',
        'age':23,
        'place': 'tvm',
    }
    return render(request,'index.html', person)

def about(request):
    number ={
        'a_list': [1,2,3],
    }
    return render(request,'about.html', number)
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form .is_valid():
            form.save()
            return render(request,'conformation.html')
            
    form=BookingForm()
    dict_form={
        'form': form
    }
    return render(request,'booking.html',dict_form)
def doctors(request):
    dict_doc={
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doc)
def contact(request):
    return render(request,'contact.html')
def department(request):
    dict_dept={
        'dept' : Department.objects.all()
    }
    return render(request,'department.html',dict_dept)
