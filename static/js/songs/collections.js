Salsasite.SongCollection=Backbone.Collection.extend({
    model:Salsasite.Song,
    url:'/api/v1/song/',


    parse:function(response){
        return response.objects
    }

 
})