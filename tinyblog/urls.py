from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import main.views


urlpatterns = [
    url(r'^$', main.views.index_view, name='index'),
    url(r'^post/', main.views.post_view, name='post'),
    url(r'^account/', main.views.account_view, name='account'),
    url(r'^login/', main.views.login_view, name='login'),
    url(r'^logout/', main.views.logout_view, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
]
