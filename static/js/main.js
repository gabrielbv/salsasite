window.Song = Backbone.Model.extend();

window.SongCollection = Backbone.Collection.extend({
    model:Song,
    url:"../api/songs"
});


window.SongListView = Backbone.View.extend({
 
    tagName:'ul',
 
    initialize:function () {
        this.model.fetch("reset", this.render, this);
    },
 
    render:function (eventName) {
        _.each(this.model.models, function (song) {
            $(this.el).append(new SongListItemView({model:song}).render().el);
        }, this);
        return this;
    }
 
});
 
window.SongListItemView = Backbone.View.extend({
 
    tagName:"li",
 
    template:_.template($('#tpl-song-list').html()),
 
    render:function (eventName) {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }
 
});
 
window.SongView = Backbone.View.extend({
 
    template:_.template($('#tpl-song-details').html()),
 
    render:function (eventName) {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }
 
});

var AppRouter = Backbone.Router.extend({

    routes:{
        "":"list",
        "song/:id":"songDetails"
    },

    list:function () {
        this.SongList = new SongCollection();
        this.SongListView = new SongListView({model:this.songList});
        this.SongList.fetch();
        $('#sidebar').html(this.SongListView.render().el);
    },

    wineDetails:function (id) {
        this.song = this.SongList.get(id);
        this.SongView = new SongView({model:this.song});
        $('#content').html(this.SongView.render().el);
    }
});

var app = new AppRouter();
/*Backbone.history.start();*/
Backbone.history.start({pushState: true});