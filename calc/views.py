from django.shortcuts import render
from .forms import Multistep
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'index.html')
def selection(request):
    return render(request,'selection.html')
def bas(request):
    if request.method=='POST':
        #b=request.POST.get("b")
        #print(b)
        b=Multistep(request.POST)

        if b.is_valid():
            b.save()
            return HttpResponseRedirect('/thanks/')
    else:
        b= Multistep()
    context = {
        'form': b,
    }
    return render(request,'bas.html',context)
def thanks(request):
    return render(request,'thanks.html')
