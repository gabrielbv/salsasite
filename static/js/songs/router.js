var AppRouter=Backbone.Router.extend({
    routes:{
        '':'list',
    },




    list:function(){

        this.songList = new SongCollection();
        this.songListView=new SongListView({model:this.songList});
        this.songList.fetch();
        /*$('#content').html(this.songListView.render().el)*/
    }


});

var app = new AppRouter();
Backbone.history.start();