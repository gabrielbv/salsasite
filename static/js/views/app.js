window.SongListView=Backbone.View.extend({
    tagName:'div',
    template: _.template($("#tpl-song-list").html()),


    initialize:function(){
        this.model.bind('reset',this.render,this)

    },

    render:function(){
        _.each(this.model.models,function(song){

        $(this.el).append(new SongListItemView({model:song}).render().el)

    },this);
        return this;
    }
});

window.SongListItemView=Backbone.View.extend({
    tagName:'div',
    template:_.template($('#tpl-song-list-item').html()),

    initialize:function(){
        this.model.bind('change',this.render,this)
    },

    render:function(){
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    },
});