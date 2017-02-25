from django.shortcuts import render
from django.http import HttpResponse
from students.models import Stud
# Create your views here.
def home(request):
    return render(request,'home.html')
def search(request):
    if 'q' in request.GET:
        q=request.GET['q']
        students=Stud.objects.filter(name__icontains=q)
        return render(request,'search.html',{'students':students})
