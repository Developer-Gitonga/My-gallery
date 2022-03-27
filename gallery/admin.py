from django.contrib import admin
from .models import Editor, Image, Category, Location


# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizantal = ('images',)

admin.site.register(Editor)
admin.site.register(Image,ImageAdmin)
admin.site.register(Category)
admin.site.register(Location)





