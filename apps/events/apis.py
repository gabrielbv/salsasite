from tastypie.resources import ModelResource
from events.models import Event
from datetime import tzinfo, timedelta, datetime
from django.utils import timezone



class EventResource(ModelResource):
    class Meta:
        queryset=Event.objects.filter(start_date__gte=timezone.now(),pub_date__lte=timezone.now(),event_status="APROVED").order_by('start_date')
        resource_name='event'

    def dehydrate_start_date(self,bundle):
        return bundle.data['start_date'].strftime('%B %d, %Y, %I:%M %p' )
         