window.Song = Backbone.Model.extend({
    
    urlRoot:"/api/v1/song/",

    defaults:{

        "id":null,
        "title":"",
        "artist":"",
        "genre":"",
        "bpm":"",
        "price":""
    }

})
