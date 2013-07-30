var AppRouter=Backbone.Router.extend({
    routes:{
        '':'list',
    },




    list:function(){

        this.songList = new SongCollection();
        this.songListView= new SongListView({collection:this.songList});

        var self = this;
        
        this.songList.fetch({
           
            success:function(){
                
               
                $('#content').html(self.songListView.render().el);

            },
        }); 
        },
     
 


});

var app = new AppRouter();
Backbone.history.start();