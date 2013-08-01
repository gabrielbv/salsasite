Salsasite.EventListView=Backbone.View.extend({
    tagName:'div',
    initialize: function() {
    this.template = _.template($('#tpl-event-list').html());
    },

 
    render:function(){
        var self=this
        
        if(this.collection.toJSON().length >0){
            console.log(this.collection)
        _.each(this.collection.models,function(event){
            

            
            $(self.el).append(self.template(event.toJSON()))

        })
    }
        else{
            $(self.el).html('No articles yet.')
        }
        return this;
        
    },
});

Salsasite.EventDetailsView=Backbone.View.extend({
    tagName:'div',

    initialize:function(){
        this.template=_.template($('#tpl-event-details').html());
    },

    render:function(event){
        $(this.el).html(this.template(this.collection.toJSON()))
        return this;
    },
})