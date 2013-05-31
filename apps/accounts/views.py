# Create your views here.
from django.contrib.auth import authenticate, login as django_login
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render , render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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

def passreset(request):

    if request.method =="POST":
        return HttpResponseRedirect(reverse("passwordreset"))

    return render(request, 'accounts/password_reset_form.html')

@login_required
def view_profile(request):

    profile = UserProfile.objects.get(user_id = request.user.id)

    return render(request, 'accounts/profile.html', {
    
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            "profile" : profile,
    
    })


   
