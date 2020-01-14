"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, re_path
from django.contrib import admin
from film.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/', movies),
    url(r'^movie_details/(?P<pk>\d+)$', film),
    url(r'persons/', persons),
    url(r'^edit_person/(?P<pk>\d+)$',edit_person),
    url(r'^add_person/',add_person),
    url(r'^edit_movie/(?P<pk>\d+)$', edit_movie),
    url(r'^add_movie/', add_movie),
    url(r'^search_movie/', search_movie),
    url(r'^count/', count),
]
