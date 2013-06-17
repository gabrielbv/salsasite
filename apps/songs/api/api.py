from tastypie.api import Api
from resources import SongResource

v1 = Api("v1")
v1.register(SongResource())