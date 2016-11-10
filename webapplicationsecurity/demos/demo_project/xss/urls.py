from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^xss_demo/$', 'xss.views.xss_first_page', name='xss_first_page'),
        )
