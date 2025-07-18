from django.shortcuts import redirect, render

from app.forms import studentform
from app.models import student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def home(request):
    gopi=student.objects.all()
    return render(request, 'app/home.html',{'gopi':gopi})
def detail(request,id):
    form=student.objects.get(id=id)
    return render(request,'app/details.html',{'form':form})
def student_name(request):
    if request.method=='POST':
        boy=studentform(request.POST)
        if boy.is_valid():
            boy.save()
    else:
      boy=studentform()
    return render(request,'app/student.html',{'boy':boy})
def register(request):
    if request.method=='POST':
        boy=UserCreationForm(request.POST)
        if boy.is_valid():
            boy.save()
            return redirect('login')
            
    boy=UserCreationForm()
    return render(request,'app/register.html',{'boy':boy})