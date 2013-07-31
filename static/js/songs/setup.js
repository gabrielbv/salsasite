 $(document).ready(function() {
    
    Salsasite.songs= new Salsasite.SongCollection()
    Salsasite.songs.fetch({
        success:function(){
            Salsasite.initialize();    
        }
    })
    
})