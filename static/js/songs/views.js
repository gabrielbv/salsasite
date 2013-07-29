window.SongListView=Backbone.View.extend({

    tagName:'div',
    template:_.template($("#tpl-song-list").html()),

    render:function(eventName){
        this.$el.html(this.template(this.model.toJSON));
        return this;

    }
});

