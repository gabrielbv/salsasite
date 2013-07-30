Salsasite.SongListView=Backbone.View.extend({

    tagName:'div',

    initialize:function(){
    this.template=_.template($("#tpl-song-list").html());
    console.log(1)
    },


    render:function(){
        var self=this
        _.each(this.collection.models,function(song){
            console.log(self.template(song.toJSON()))
            $(self.el).append(self.template(song.toJSON()));

        })
        return this;
    }
    

    
});
