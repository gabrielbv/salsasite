window.Song = Backbone.Model.extend({
    /*urlRoot:"/api/v1/song/",*/
    

    url: function() {


        if (this.get('id') != null){

        var url="/api/v1/song/"+this.get("id")+"/"

        }

        else

        {

            var url="/api/v1/song/"
        }

    return url


    },

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
    url:"/api/v1/song/",

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
        
        "click .mysongs":"mysongs",
        
        "click .aproved":"selectaproved",
        "click .rejected": "selectrejected",
        "click .pending":"selectpending",
        "click .draft":"selectdraft",

              
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


    mysongs:function(event){
        app.navigate("mysongs",true)
        return false;
    },

    selectaproved:function(event){
        console.log("status")      
        app.navigate("status/aproved/",true);

        return false;
    },    
    selectrejected:function(event){
              
        app.navigate("status/rejected/",true);

        return false;
    },
    selectpending:function(event){
              
        app.navigate("status/pending/",true);

        return false;
    },
    selectdraft:function(event){
              
        app.navigate("status/draft/",true);

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

            app.songList.create(self.model, {
                success:function(){

                    app.navigate("confirm", true);    

                }
            });

        } else 

        {

            var self=this
            self.model.save({
                success: function () {
                    app.navigate("", true);  

                    /*return false  */
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
        'mysongs':'upsongs',
        'confirm':"confirmSong",
        'status/:status/':'upsongs',   
        'genre/:genre/':'list',
        ':id/': "songDetails",
        ':id/edit':"songEdit",
        ':id/buy' : "songBuy",




    },

    initialize:function () {

        this.songList = new SongCollection();
        /*this.songList.fetch();*/
        console.log("initialize", $('#header'));

        $('#header').html(new HeaderView().render().el);

        console.log($('#header').html())

    },



    list:function(genre, status){
        console.log("list",genre)
        
        var self=this;
        
        data = {}
        if (status != undefined){
            data['status'] = status

        }

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

        if ( USER_ID == null){

            window.location = "/accounts/login/"
            return false

        };

        this.currentSong = new Song({id:id});

        console.log(this.currentSong.get("id"));   

        self=this

        this.currentSong.fetch({ 

            success:function(){ 

            self.songEditView = new SongEditView({model:self.currentSong});

            $('#content').html(self.songEditView.render().el);

            },
        });


    },

    confirmSong:function(){

        console.log("confirmation");
        $('#header').html("The new song has been saved. Please wait for administrator to approve it");
    },

    upsongs:function(status){
        genre=undefined
        this.songList.url="/api/v1/usersongs/";
        this.list(undefined,status)
        
    }


});
    
var app = new AppRouter();
Backbone.history.start();

