window.Song = Backbone.Model.extend({
                 
    });

window.SongCollection=Backbone.Collection.extend({
    model:Song,
    url:"/api/song/",

    parse:function(response){
        return response.objects
    }
});

window.SongListView = Backbone.View.extend({
    tagName:"ul",

    initialize:function(){
        this.model.bind("reset",this.render,this);

    },
    render:function(eventName){
        console.log(1)
        console.log(this.model.models.length)
        _.each(this.model.models,function(song){
            console.log(2)
            $(this.el).append(new SongListItemView({model:song}).render().el);

        },this);
        return this;
    }
});

window.SongListItemView = Backbone.View.extend({
    tagName: "li",

    template:_.template($("#tpl-song-list-item").html()),

    render:function(eventName){
        console.log(3)
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }
});

window.SongView = Backbone.View.extend({
    template : _.template($('#tpl-song-details').html()),
    render:function(eventName){
        $(this.el).html(this.template(this.model.toJSON()));
        return this;

    }

});

window.NewSong= Backbone.View.extend({
    template:_.template($('#tpl-new').html()),
    
    initialize:function(){
        this.render();
    },

    render:function(eventName){
        $(this.el).html(this.template());
        return this;
    },

    events:{
        "click .new":"newSong"
    },

    newSong:function(event){
        app.navigate("new",true);
        return false;
    }
})

var AppRouter = Backbone.Router.extend({
    routes:{
        '': "list",
        ':id': "songDetails",
        'new':"newSong"

    },
    
    list:function(){
        
        this.songList = new SongCollection();
        var self=this;

        
        this.songList.fetch({
            success:function(){
                
                self.songListView = new SongListView({model:self.songList});
                $("#sidebar").html(self.songListView.render().el);

            },
        });

    },


    songDetails:function(id){
        if (this.songList){

            this.song = this.songList.get(id);
            this.songView = new SongView({model:this.song});
            $('#content').html(this.songView.render().el);

        }

    },

    newSong:function(){
        this.songView = new SongView({model:new Song()});
        $('#content').html(this.songView.render().el);
    }


});

var app = new AppRouter();
Backbone.history.start();

       