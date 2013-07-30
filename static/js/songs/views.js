window.SongListView=Backbone.View.extend({

    tagName:'div',
    template:_.template($("#tpl-song-list").html()),

    initialize:function(){
        this.collection.bind('reset',this.render,this);

    }


    render:function(eventName){
        _.each(this.model.models,function(song){
            $(this.el).append(new SongListItemView({collection:song}).render().el);
        },this);
        return this;
    }
    

    
});

window.SongListItemView=Backbone.View.extend({
    tagName:'div'
    template:_.template($('tpl-song-item').html()),

    render:function(eventName){
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }
})
