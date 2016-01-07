from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'apps.hello.views.person_view', name='person_view'),
    url(r'^admin/', include(admin.site.urls)),
)
