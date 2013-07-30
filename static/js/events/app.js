window.Salsasite={};

Salsasite.initialize=function(){

    var app = new Salsasite.AppRouter();
    Backbone.history.start();
}