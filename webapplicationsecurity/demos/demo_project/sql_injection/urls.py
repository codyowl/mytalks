from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^sql_injection/$', 'sql_injection.views.sql_injection_first_page',name='sql_injection_first_page'),
        )
