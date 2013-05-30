# Create your views here.
from django.contrib.auth import authenticate, login as django_login
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render , render_to_response
from django.contrib import messages

from accounts.forms import UserForm
from accounts.models import UserProfile

def register(request):
    
    form = UserForm()
    if request.method == "POST":
    	form = UserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            profile = UserProfile.objects.create(
                user=user,
                country=form.cleaned_data.get('country')
            )
            
            return HttpResponseRedirect(reverse("register"))
        
    return render(request, 'accounts/register.html', {'form': form})

def user_edit(request):

    if request.method == "POST":
        return HttpResponseRedirect(reverse("user_edit"))

    return render(request, 'accounts/user_edit.html')
