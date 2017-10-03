# Django imports
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

# modules
from rest_framework.urlpatterns import format_suffix_patterns

#local imports
from main.views import detail_view

app_name ='main'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^content/$', TemplateView.as_view(template_name='content.html')),
    url(r'^react-content/$', TemplateView.as_view(template_name='react-content.html')),
    url(r'^api/(?P<pk>\d+)$', views.detail_view.as_view()),
    url(r'^api/list/$', views.list_view.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
