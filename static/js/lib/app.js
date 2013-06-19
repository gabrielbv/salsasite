window.Song = Backbone.Model.extend({
    defaults:{
        "id":null,
        "title":"",
        "artist":"",
        "genre":"",
        "bpm":"",
        "price":""
    }     
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
        var self = this;
    },
    render:function(eventName){
      
        console.log(this.model.models.length)
        _.each(this.model.models,function(song){
           
            $(this.el).append(new SongListItemView({model:song}).render().el);

        },this);
        return this;
    }
});

window.SongListItemView = Backbone.View.extend({
    tagName: "li",

    template: _.template($("#tpl-song-list-item").html()),

    initialize:function () {
        this.model.bind("change", this.render, this);
    },

    render:function(eventName){
      
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }
});

window.SongView = Backbone.View.extend({
    template : _.template($('#tpl-song-details').html()),
    render:function(eventName){
        $(this.el).html(this.template(this.model.toJSON()));
        return this;

    },

    events:{
        
        "click .edit":"editSong",
        "click .store": "purchaseSong"
        
    },

    editSong:function(event){
              
        app.navigate(this.model.id+"/edit",true);
        
        return false;
    },

    purchaseSong:function(event){

        window.location="/purchases/"+this.model.id+"/";

        return false;
    }

});


window.SongEditView = Backbone.View.extend({
    template:_.template($('#tpl-song-edit').html()),


    render:function (eventName) {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    },

    events:{
        "click .save":"saveSong"
        
    },

    saveSong:function(){
        
        this.model.set({
            title:$('#title').val(),
            artist:$('#artist').val(),
            genre:$('#genre').val(),
            bpm:$('#bpm').val(),
            price:$('#price').val()
        })


        
        if(this.model.isNew()){
    

            var self=this;

            app.songList.create(this.model,{
                success:function(){

                    app.navigate('', true);    

                }
            });

        } else {
            this.model.save();
        }

        return false;
    },


});



window.HeaderView= Backbone.View.extend({
    template:_.template($('#tpl-new').html()),
    
    initialize:function(){
        this.render();
    },

    render:function(eventName){
        console.log(11)
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
});



var AppRouter = Backbone.Router.extend({
    routes:{
        '': "list",
        'new':"newSong",
        ':id': "songDetails",
        ':id/edit':"songEdit",
        ':id/buy' : "songBuy"
        

    },

    initialize:function () {
        $('#header').html(new HeaderView().render().el);
    },


    
    list:function(){
        console.log("list")
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

        
        this.songEditView = new SongEditView({model:new Song()});
        $('#content').html(this.songEditView.render().el);
    },

    songEdit:function(id){

        this.song = this.songList.get(id);
        this.songEditView = new SongEditView({model:this.song});
        $('#content').html(this.songEditView.render().el);

    }


});

var app = new AppRouter();
Backbone.history.start();

       