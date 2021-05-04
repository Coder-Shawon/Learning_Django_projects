from django.contrib import admin

from .models import Myalbum 
# Register your models here.


class MyalbumAdmin(admin.ModelAdmin):

    list_display = [
        'description',
        'thumbnail',
        'creation'
        


    ]


admin.site.register(Myalbum, MyalbumAdmin)

