from cms_site.urls import *


urlpatterns = [
    url(r'^photologue/', include('photologue.urls')),
] + urlpatterns
