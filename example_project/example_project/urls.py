from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from things.views import CreateThingView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', CreateThingView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
