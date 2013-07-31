Salsasite.SongListView=Backbone.View.extend({

    tagName:'div',

    initialize:function(){
    this.template=_.template($("#tpl-song-list").html());
    
    },


    render:function(){
        var self=this
        
        _.each(this.collection.models,function(song){

            $(self.el).append(self.template(song.toJSON()));

        })
        return this;
    }
    

    
});
