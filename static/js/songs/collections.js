window.SongCollection=Backbone.Collection.extend({
    model:Song,
    url:'/api/v1/song/',


    parse:function(response){
        return response.objects
    }

 
})