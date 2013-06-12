window.SongListView = Backbone.View.extend({
 
    tagName:'ul',
 
    initialize:function () {
        this.model.bind("reset", this.render, this);
    },
 
    render:function (eventName) {
        _.each(this.model.models, function (song) {
            $(this.el).append(new WineListItemView({model:song}).render().el);
        }, this);
        return this;
    }
 
});
 
window.SongListItemView = Backbone.View.extend({
 
    tagName:"li",
 
    template:_.template($('#tpl-wine-list-item').html()),
 
    render:function (eventName) {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }
 
});
 
window.SongView = Backbone.View.extend({
 
    template:_.template($('#tpl-wine-details').html()),
 
    render:function (eventName) {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }
 
});