from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # On include() Django will forward the url to the URLConf object chopping
    # the part that matched initially. So for example in this case won't send 
    # /polls/<whatever>, but just <whatever> to polls.urls
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
)
