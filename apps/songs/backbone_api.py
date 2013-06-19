# fooapp/backbone_api.py
import backbone
from songs.models import Song

class SongAPIView(backbone.views.BackboneAPIView):
    model = Song
    display_fields = ('artist', 'title')

backbone.site.register(SongAPIView)


AddEditView = Backbone.View.extend({
render: function(){
 # various jquery template things, here
Backbone.ModelBinding.call(this);
}
});