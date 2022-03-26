# from email.mime import image
# from unicodedata import category
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from . import views

urlpatterns=[
    url('',views.imagedisplay)
    # url(r'^search/', views.search_results, category='search_results')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)