from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .forms import *
from .models import *
from .forms import studentForm, personlinfoForm
from .models import student, personlinfo
from django.urls import reverse, reverse_lazy
# Create your views here.
def home(request):
    obj=student.objects.all()
    return render(request, 'home.html',{'data':obj})



def create(request):
    if request.method == 'POST':
        fm = studentForm(request.POST)
        pr=personlinfoForm(request.POST)
        if fm.is_valid() and pr.is_valid():
            fm.save()
            #pr.instance = fm
            pr.save()
            return redirect("read")
    else:
        fm = studentForm()
        pr = personlinfoForm()
    return render(request,'index.html',{'fm':fm,'pr':pr})


def update(request, pk):
    obj = student.objects.get(pk=pk)
    fm = studentForm(instance=obj)
    if request.method == 'POST':
        fm = studentForm(request.POST, instance=obj)
        if fm.is_valid():
            fm.save()
            return redirect('read')
    template_name = 'update.html'
    context = {'fm': fm}
    return render(request, template_name, context)

def delete(request, id):
    obj=student.objects.filter(id=id)
    obj.delete()
    HttpResponse("deleted successfully")
    return redirect('read')

def personal(request, id):
    task = personlinfo.objects.filter(id=id)
    return render(request, "personal.html", { "task": task })
    return redirect('read')

def add(request):
    #obj = personlinfo.objects.get(pk=pk)
    #pr = personlinfoForm(instance=obj)
    if request.method == 'POST':
        pr=personlinfoForm(request.POST)
        if  pr.is_valid():
            
            pr.save()
            return redirect("person")
    else:
       
        pr = personlinfoForm()
    return render(request,'add.html',{'pr':pr})