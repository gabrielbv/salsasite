 $(document).ready(function() {
    
    Salsasite.events= new Salsasite.EventCollection()
    Salsasite.events.fetch({
        success:function(){
            Salsasite.initialize();    
        }
    })
    
})