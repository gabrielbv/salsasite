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
    tagName:"div",
    template: _.template($("#tpl-song-list").html()),

    
    events:{
        
        "click .bachata":"selectbachata",
        "click .kizomba": "selectkizomba",
        "click .salsa":"selectsalsa",
              
    },  

    selectbachata:function(event){
        console.log("bachata")
        app.navigate("genre/bachata/",true);

        return false;
    },

    selectkizomba:function(event){
        app.navigate("genre/kizomba/",true);

        return false;
    },

    selectsalsa:function(event){
              
        app.navigate("genre/salsa/",true);

        return false;
    },

    initialize:function(){

        this.model.bind("reset",this.render,this);
        _.bindAll(this,"selectbachata");
        var self = this;
    },
    render:function(eventName){
      
            

        
        $(this.el).html(this.template());
       
        _.each(this.model.models,function(song){
           
            $(this.el).append(new SongListItemView({model:song}).render().el);

        },this); 

        return this;
    }



});

window.SongListItemView = Backbone.View.extend({
    tagName: "div",

    template: _.template($("#tpl-song-list-item").html()),

    initialize:function () {
        this.model.bind("change", this.render, this);
    },

    events:{
        
        "click .edit":"editSong",
        "click .store": "purchaseSong",
        "click .play":"songPlay",
        "click .pause": "songPause",

        
    },

    editSong:function(event){
              
        app.navigate(this.model.id+"/edit",true);

        return false;
    },

    purchaseSong:function(event){
        window.location="/purchases/"+this.model.id+"/";

        return false;
    },

    songPlay:function(){

        var mySound = soundManager.createSound({
            id: "id_"+this.model.get('id'),
            url: this.model.get('music_file') // path to stream
            }).play()
    },


    songPause:function(){

        var mySound = soundManager.createSound({
            id: "id_"+this.model.get('id'),
            url: this.model.get('music_file') // path to stream
            }).pause()
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

            app.songList.create(this.model, {
                success:function(){

                    app.navigate("confirm", true);    

                }
            });

        } else 

        {
            this.model.save(null, {
                success: function () {
                    app.navigate("", true);    
                }
            });

        }

        return false;
    }


});



window.HeaderView= Backbone.View.extend({
    template:_.template($('#tpl-new').html()),
    
    initialize:function(){
        this.render();
    },

    render:function(eventName){
        console.log("render")
        $(this.el).html(this.template());
        console.log($(this.el).html())
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
        'confirm':"confirmSong",
        'genre/:genre/':'list',
        ':id/': "songDetails",
        ':id/edit':"songEdit",
        ':id/buy' : "songBuy",




    },

    initialize:function () {

        this.songList = new SongCollection();
        console.log("initialize", $('#header'));

        $('#header').html(new HeaderView().render().el);

        console.log($('#header').html())

    },



    list:function(genre){
        console.log("list",genre)
        
        var self=this;
        
        data = {}
        if (genre != undefined){
            data['genre'] = genre
        }

        this.songList.fetch({
            data: data,
            success:function(){
                
                console.log("success");

                self.songListView = new SongListView({model:self.songList});
                $("#content").html(self.songListView.render().el);

            },
        });

    },


    songDetails:function(id){

        console.log("songDetails");

        if (this.songList){

            console.log("songList");

            this.song = this.songList.get(id);
            this.songView = new SongView({model:this.song});

            $('#content').html(this.songView.render().el);

        };

    },

    newSong:function(){

        console.log("newSong");
        
        this.songEditView = new SongEditView({model:new Song()});
        $('#header').html(this.songEditView.render().el);
    },

    songEdit:function(id){

        console.log("songEdit");

        this.song = this.songList.get(id);
        this.songEditView = new SongEditView({model:this.song});
        $('#content').html(this.songEditView.render().el);

    },

    confirmSong:function(){

        console.log("confirmation");
        $('#header').html("The new song has been saved. Please wait for administrator to approve it");
    }


});


var app = new AppRouter();
Backbone.history.start();
       