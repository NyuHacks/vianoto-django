from django.contrib import admin
from django.conf.urls import patterns, include, url

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^$', 'apps.video.views.home'),
    url(r'^login', 'apps.video.views.loginview'),
    url(r'^auth', 'apps.video.views.auth_and_login'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
