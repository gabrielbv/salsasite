window.SongCollection=Backbone.Collection.extend({
    model:Song,
    url:'/api/v1/song',


    parse: function (resoponse){
        return resoponse.objects;
    }


})