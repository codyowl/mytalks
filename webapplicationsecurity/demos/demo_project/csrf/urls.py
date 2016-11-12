from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
            url(r'^csrf_demo/$', 'csrf.views.csrf_first_page', name'csrf_first_page'),
            )

