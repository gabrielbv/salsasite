from tastypie.resources import ModelResource
from my_app.models import MyModel


class MyModelResource(ModelResource):
    class Meta:
        queryset = MyModel.objects.all()
<<<<<<< HEAD
        allowed_methods = ['get']

=======
        allowed_methods = ['get']
>>>>>>> 559b7e467850fc72e7584bd5ae2ea333782a01e3
