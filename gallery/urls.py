# from email.mime import image
# from unicodedata import category
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from . import views

urlpatterns=[
   
    # url('',views.image_upload, name = 'image_upload'),
    url('search/', views.search_results, name='search_image'),
    url('',views.index)
    # url(r'^search/', views.search_results, category='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)