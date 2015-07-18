from django.conf.urls import patterns, include, url
from django.contrib import admin
from grocery_list import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assignment_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^item/(?P<item_id>\d+)$', views.item, name='detail'),
    url(r'^list/$', views.items_list, name='items_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cat/(?P<cats>.*)$', views.items_cats, name='items_list'),
)
