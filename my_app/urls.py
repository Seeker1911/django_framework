from django.conf.urls import url
from . import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^app$', views.index, name='index'),
    url(r'^ash$', views.home, name='home'),
]
