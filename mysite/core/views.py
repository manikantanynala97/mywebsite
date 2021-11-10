from django.forms import fields
from django.http import request
from django.http  import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_list_or_404
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import JsonResponse
import json                              
from .forms import GeeksForm
import requests
from .models import GeeksModel

API_KEY='87628851ebb44aec81cdd3c898b6db63'
# Create your views here.

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    language = request.GET.get('language')


    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    elif category :
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    else :
        url = f'https://newsapi.org/v2/top-headlines?language={language}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    count = User.objects.count()
    return render(request,'home.html',{'count':count,'articles':articles})

def signup(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
        return render(request,'registration/signup.html',{'form':form})  



def create_blog(request):
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_blog')
    return render(request,'blog_form.html',{'form':form})


def list_blog(request):
     blog = GeeksModel.objects.all()
     return render (request,'list_blog.html',{'blog':blog})


def update_blog(request,id):
    blog = GeeksModel .objects . get(id = id)
    form = GeeksForm(request.POST or None , instance=blog)
    if form.is_valid():
        form.save()
        return redirect('list_blog')
    return render(request,'blog_form.html',{'form':form,'blog':blog})


    

def delete_blog(request,id):
    blog = GeeksModel.objects.get(id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('list_blog')
    return render(request,'delete_blog.html',{'blog':blog})    



def json(request):
    data = list(GeeksModel.objects.values())
    return JsonResponse(data,safe=False)

     

    
          
      
