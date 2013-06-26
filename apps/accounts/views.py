    # Create your views here.
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render , render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from accounts.forms import UserForm,UserEdit
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
            
            return HttpResponseRedirect(reverse("profile"))
        
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def user_edit(request):
        
    profile = UserProfile.objects.get(user=request.user)
    form = UserEdit(instance=request.user,initial={'country':profile.country })
    if request.method == "POST":
        form = UserEdit(request.POST,instance=request.user)

        if form.is_valid():
            user = form.save()
            profile.country=form.cleaned_data.get('country')
            profile.save()

        
            return HttpResponseRedirect(reverse("user_edit"))

    return render(request, 'accounts/user_edit.html', {'form': form})

@login_required
def view_profile(request):

    profile = UserProfile.objects.get(user_id = request.user.id)


    return render(request, 'accounts/profile.html', {
    
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            "profile" : profile,
    
    })


