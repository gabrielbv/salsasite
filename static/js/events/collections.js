Salsasite.EventCollection=Backbone.Collection.extend({
    model:Salsasite.Event,
    url:'/api/v1/event/',
    parse:function(response){
        return response.objects
    }
})