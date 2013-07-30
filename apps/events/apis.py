from tastypie.resources import ModelResource
from events.models import Event


class EventResource(ModelResource):
    class Meta:
        queryset=Event.objects.all().order_by('id')
        resource_name='event'