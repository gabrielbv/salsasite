# Create your views here.
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render , render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from musicmanage.models import MusicManage
from musicmanage.forms import SongsForm



#@login_required
def view_music_manage(request):

    form = SongsForm()
    if request.method == "POST":
    	form = SongsForm(request.POST)
        
        if form.is_valid():
            MusicManage = form.save()
            
            profile = MusicManage.objects.create(
                music=MusicManage,
            )
            
            return HttpResponseRedirect(reverse("login"))
        
    return render(request, 'accounts/register.html', {'form': form})


