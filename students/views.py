from django.shortcuts import render
from django.http import HttpResponse
from students.models import Stud
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    return render(request,'home.html')
def search(request):
    if 'q' in request.GET:
        q=request.GET['q']
        if 'page' in request.GET:
            page=request.GET['page']
        else:
            page =1
        
        students=Stud.objects.filter(name__icontains=q) or Stud.objects.filter(roll__icontains=q)
        students=students.order_by('roll')
        paginator=Paginator(students,10)

        try:
            students= paginator.page(page)
        except PageNotAnInteger:
            students=paginator.page(1)
        except EmptyPage:
            students=paginator.page(paginator.num_pages)
            
        return render(request,'search.html',{'students':students})
