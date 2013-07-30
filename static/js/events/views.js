/*Salsasite.EventListItemView=Backbone.View.extend({
    tagName:'div',
    initialize: function() {
        _each.()
    this.template = _.template($('#tpl-event-list').html());
    },


    render:function(){
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
    }
    
})*/

Salsasite.EventListView=Backbone.View.extend({
    tagName:'div',
    initialize: function() {
    this.template = _.template($('#tpl-event-list').html());
    },

 
    render:function(){
        var self=this
        _.each(this.collection.models,function(event){
            console.log($(self.el).html())
            $(self.el).append(self.template(event.toJSON()))
        })
        return this;
        
    },
})