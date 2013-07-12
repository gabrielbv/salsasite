from django.contrib import admin
from news.models import News



class NewsAdmin(admin.ModelAdmin):

    list_display = ("title" , "status", "user", "published")
    list_filter = ("status","published",)


admin.site.register(News, NewsAdmin)
