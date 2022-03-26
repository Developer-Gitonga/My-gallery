from django.contrib import admin
from .models import Editor, Image,


# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizantal = ('images',)

admin.site.register(Editor)
admin.site.register(Image,ImageAdmin)





