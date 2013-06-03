# Create your views here.
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render , render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def view_music_manage(request):

    profile = UserProfile.objects.get(user_id = request.user.id)


    return render(request, 'music/music_manage.html', {
    
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            "profile" : profile,
    
    })
