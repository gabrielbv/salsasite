Salsasite.AppRouter = Backbone.Router.extend({
    routes:{
        "":'list',
        ':id/':'event_details'
    },


    list:function(){

        this.eventListView = new Salsasite.EventListView({collection:Salsasite.events})
      
        $('#content').html(this.eventListView.render().el)
    },

    event_details:function(id){
        this.event=Salsasite.events.get(id)

        this.eventDetailsViews= new Salsasite.EventDetailsView({collection:this.event})
        $('#content').html(this.eventDetailsViews.render().el)
    }
})

