from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   return render(request,"1.html")

def display(request):
    num1=int(request.GET["n1"])
    if num1 >18:
        return render(request,"2.html") 
    else:
        #  return render(request,"1.html",{'key':"you are not eligible"}) 
         return HttpResponse("you are not eligible") 