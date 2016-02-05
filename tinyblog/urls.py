from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import tinyblog.views


urlpatterns = [
    url(r'^$', tinyblog.views.index_view, name='index'),
    url(r'^post/', tinyblog.views.post_view, name='post'),
    url(r'^account/', tinyblog.views.account_view, name='account'),
    url(r'^login/', tinyblog.views.login_view, name='login'),
    url(r'^logout/', tinyblog.views.logout_view, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
]
