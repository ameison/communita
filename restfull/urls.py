from django.conf.urls import url, include 
import restfull.apirest.urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    url(r'', include(restfull.apirest.urls)),

] 

