# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from accounts.forms import UserForm
from django.shortcuts import render

def register(request):
    
    form = UserForm()
    if request.method == "POST":
    	form = UserForm(request.POST)
        
        if form.is_valid():
        	form.save()
        	return HttpResponseRedirect(reverse("register"))
        
    return render(request, 'accounts/register.html', {'form': form})
