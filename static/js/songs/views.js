window.SongListView=Backbone.View.extend({

    tagName:'div',
    template:_.template($("#tpl-song-list").html()),

    render:function(){

        this.$el.html(this.template(this.model.toJson));
        
        return this;

    }
});

