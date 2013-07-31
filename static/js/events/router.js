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

        this.eventListView = new Salsasite.EventListView({collection:Salsasite.events})
        
        this.event=this.eventListView.toJSON().id;
        
        this.eventDetailsView=new Salsasite.EventDetailsView({collection:Salsasite.events})
        
        $('#content').html(this.eventDetailsView.render().el)
    }
})


