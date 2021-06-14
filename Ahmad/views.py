from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList ,Item

# Create your views here.
def index (response ):
    ls =ToDoList.objects.get(id=id)
    return render(response,"Ahmad/base.html",{} )







def home (response):
    return render(response,"Ahmad/home.html",{} )


