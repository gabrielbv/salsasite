var AppRouter=Backbone.Router.extend({
    routes:{
        '':'list'
    },


    initialize:function(){

        this.songList=new SongCollection()

            $('#header').html(new HeaderView().render().el);

        
    },

    list:function(){
        this.songListView=new songListView({model:this.songList});
        this.songList.fetch();
    }


});

var app = new AppRouter();
Backbone.history.start();