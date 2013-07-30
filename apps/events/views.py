# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect ,Http404
from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from events.models import Event
from events.forms import EventForm




def list(request):

   
    events=Event.objects.filter(start_date__gte=timezone.now(),pub_date__lte=timezone.now(),event_status="APROVED").order_by('start_date')

    return render (request,'events/event_list.html',{'events':events})

@login_required
def my_events(request):

    events = Event.objects.filter(user =request.user)

    return render (request,'events/my_events.html',{'events':events})


def event_view(request,slug,event_id):
    try:
        event=Event.objects.get(pk=event_id)
    except Event.DoesNotExist:

        raise Http404

    if request.user !=event.user and event.event_status not in ['APROVED']: 
        raise Http404

    return render(request,'events/details.html',{'event':event})





@login_required
def change(request, slug=None, event_id=None):
    event = None
    if event_id is not None:

        try:
            event =Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            raise Http404

        if event.event_status not in ["DRAFT","PENDING"] or request.user !=event.user:
            raise Http404

    form=EventForm(instance=event)

    if request.method == 'POST':
        form=EventForm(request.POST,instance=event)

        if form.is_valid():
            event=form.save(commit=False)
            event.user=request.user
            event.save()
            return HttpResponseRedirect (reverse ('event_details',args=[event.slug,event.id]))
        
    template = 'events/change.html'

    return render(request, template,{'form':form, 'event': event})


def backbone(request):
    return render(request,'events/events.html')

# @login_required
# def add_event(request):

#     if request.method == 'POST':

#         form=EventForm(request.POST)
#         if form.is_valid():
#             event=form.save(commit=False)
#             event.user=request.user
            

#             event.save()


#             return HttpResponseRedirect (reverse ('event_details',args=[event.slug,event.id]))
        
#     else:
#         form=EventForm()

#     return render(request,'events/add_event.html',{'form':form,}) 


# @login_required
# def event_edit(request,slug,event_id):


#     try:
#         event=Event.objects.get(pk=event_id)
#     except Event.DoesNotExist:
#         raise Http404

#     if event.event_status not in ["DRAFT","PENDING"] or request.user !=event.user:
#         raise Http404

    # form=EventForm(instance=event)

    # if request.method =='POST':
    #     form=EventForm(request.POST,instance=event)

    #     if form.is_valid():
    #         event=form.save()
    #         return HttpResponseRedirect(reverse('event_details',args=[event.slug,event.id]))

    # return render(request,'events/event_edit.html',{'form':form,'event':event})



# def generic_list(request, is_private=False):
    # print __file__, 'generic list'
    # filters = {}
    # template = 'events/my_events.html'
    # if is_private:
    #     if not request.user.is_authenticated():
    #         return HttpResponseRedirect(reverse('login'))
    #     filters['user'] = request.user
    # else:
    #     filters['start_date__gte']=timezone.now()
    #     filters['pub_date__lte']=timezone.now()
    #     filters['event_status']="APROVED"
    #     template = 'events/event_list.html'


    # events=Event.objects.filter(**filters).order_by('start_date')

    # return render (request,template,{'events':events})


