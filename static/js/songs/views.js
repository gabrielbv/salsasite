window.SongListView=Backbone.View.extend({

    tagName:'div',
    template:_.template($("#tpl-song-list").html()),


    render:function(eventName){
        _.each(this.collection.models,function(){
            $(this.el).append(this.collection({collection:song}).render().el);
        },this);
        return this;
    }
    

    
});

