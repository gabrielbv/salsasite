var AppRouter=Backbone.Router.extend({
    routes:{
        '':'list',
    },




    list:function(){

        this.songList = new Salsasite.SongCollection();
        this.songListView= new Salsasite.SongListView({collection:this.songList});
         $('#content').html(this.songListView.render().el);
        var self = this;
        

        },
     
 


});

