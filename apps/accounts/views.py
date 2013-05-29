# Create your views here.
from django.contrib.auth import authenticate, login as django_login
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render , render_to_response

from accounts.forms import UserForm
from accounts.forms import UserLogin
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


def login(request):

    form = UserLogin()

    if request.method == "POST":
        
        form = UserLogin(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
           

            user = authenticate(username=username, password=password)
            

            if user is not None:
                
                if user.is_active:
                    
                    django_login(request, user)
                    
                    return HttpResponseRedirect(reverse("login"))
                else:
                    return "Disable Account"
                            

    return render(request, 'accounts/auth.html', {'form': form}) 