var AppRouter=Backbone.Router.extend({
    routes:{
        '':'list',
    },




    list:function(){

        this.songList = new SongCollection();
        this.songListView= new SongListView({collection:this.songList});
        this.songList.fetch({
            success:function(){
                
                text =this.$el.html(this.template({songs:this.collection.toJSON}));
                console.log(text)

                $('#content').html(this.songListView.render().el);

            },
        }); 
        },
     

 


    


});

var app = new AppRouter();
Backbone.history.start();