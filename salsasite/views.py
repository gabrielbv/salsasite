from django.conf.urls.defaults import *
from django.shortcuts import render , render_to_response



def home(request):
	
	return render(request, 'home.html')

def news(request):
	
	return render(request, 'news.html')

def gallery(request):
	
	return render(request, 'gallery.html')
        
def Pdetails(request):
	
	return render(request, 'Pdetails.html')
    