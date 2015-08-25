from django.conf.urls import patterns, include, url
from django.contrib import admin
from grocery_list import views
from django.views.generic import ListView
from grocery_list.models import Item

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assignment_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^item/(?P<pk>\d+)$', views.item, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/(?P<cat>.*)$', views.ItemList.as_view(), name='items_list'),
    url(r'^item/(?P<pk>\d+)/edit/$', views.ItemUpdate.as_view(template_name="grocery_list/item_updateform.html"),  name='item_update'),
    url(r'^item/(?P<pk>\d+)/delete/$', views.ItemDelete.as_view(),  name='item_delete'),
    url(r'^add/$', views.MyView.as_view()),
    url(r'^accounts/', include('accounts.urls')),
)