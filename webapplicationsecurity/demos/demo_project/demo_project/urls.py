from django.conf.urls import patterns, include, url
from django.contrib import admin
from xss.

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        (r'^xss/', include('demo_project.xss.urls')),
)        
