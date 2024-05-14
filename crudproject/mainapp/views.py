from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request,'index.html',context)

def add_item(request):
    if request.method=="POST":
        name= request.POST['name']
        description= request.POST['description']
        item = Item(name = name,description=description)
        item.save()
        messages.info(request,"ITEM ADDED SUCCESFULLY")
    else:
        pass
    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request,'index.html',context)


def delete_item(request, myid):
    item = Item.objects.get(id=myid)
    item.delete()
    messages.info(request, "ITEM DELETED SUCCESSFULLY")
    return redirect(reverse('index'))

def edit_item(request, myid):
    sel_item = Item.objects.get(id=myid)
    item_list = Item.objects.all()
    context = {
        'sel_item':sel_item,
        'item_list': item_list
    }
    return render(request,'index.html',context)
    
def update_item(request, myid):
     item = Item.objects.get(id=myid)
     item.name = request.POST['name']
     item.description = request.POST['description']
     item.save()
     messages.info(request, "ITEM UPDETED SUCCESSFULLY")
     return redirect(reverse('index'))
     
    