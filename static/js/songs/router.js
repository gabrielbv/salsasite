Salsasite.AppRouter=Backbone.Router.extend({
    routes:{
        '':'list',
    },




    list:function(){

        this.songListView= new Salsasite.SongListView({collection:Salsasite.songs})
        console.log(this.songListView)
        $('#content').html(this.songListView.render().el);


          

        },
     
 


})



