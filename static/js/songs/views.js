window.SongListView=Backbone.View.extend({

    tagName:'div',
    template:_.template($("#tpl-song-list").html()),

    render:function(eventName){
        text =this.$el.html(this.template({songs: this.collection.toJSON}));
        console.log(text)
        return this;

    }
});

