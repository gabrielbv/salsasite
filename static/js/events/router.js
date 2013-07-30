Salsasite.AppRouter = Backbone.Router.extend({
    routes:{
        "":'list'
    },


    list:function(){

        this.eventListView = new Salsasite.EventListView({collection:Salsasite.events})
        
        $('#content').html(this.eventListView.render().el)



    },
})


