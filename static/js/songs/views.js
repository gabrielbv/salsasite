window.SongListView=Backbone.View.extend({

    tagName:'div',
    template:_.template($("#tpl-song-list").html()),

    render:function(eventName){
        this.$el.html(this.template(this.collection.toJSON));
       var text =this.$el.html(this.template({songs: this.collection.toJSON}));;
        console.log('text');
        return this;

    }
});

