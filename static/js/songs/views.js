window.SongListView=Backbone.View.extend({
    tagName:'div',
    template:_.template($("#tpl-song-list").html()),


    initialize:function(){
        this.model.bind('reset',this.render,this)

    },

    render:function(){
    this.$el.html(this.template(this.model.attributes));
    return this;

    }
});

