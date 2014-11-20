from django.conf.urls import *
from flickr.photo.models import *

urlpatterns = patterns('flickr.photo.views',
   (r"^(\d+)/$", "album"),
   (r"^(\d+)/(full|thumbnails|edit)/$", "album"),
   (r"^update/$", "update"),
   (r"^search/$", "search"),
   (r"^image/(\d+)/$", "image"),
   (r"", "main"),
)