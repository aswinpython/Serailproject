from django.http import HttpResponse
from django.shortcuts import render, redirect

from.forms import SerailForm
from.models import Serail


# Create your views here.
def index(request):
    serail=Serail.objects.all()
    context={
        'serail_list':serail
    }
    return render(request,'index.html',context)
def detail(request,serail_id):
    serail=Serail.objects.get(id=serail_id)
    return render(request,"detail.html",{'serail':serail})
def add_serail(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        serail=Serail(name=name,desc=desc,year=year,img=img)
        serail.save()
    return render(request,'add.html')
def update(request,id):
    serail=Serail.objects.get(id=id)
    form=SerailForm(request.POST or None,request.FILES,instance=serail)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'serail':serail})
def delete(request,id):
    if request.method=="POST":
        serail=Serail.objects.get(id=id)
        serail.delete()
        return redirect('/')
    return render(request,'delete.html')

