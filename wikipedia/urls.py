"""
URL configuration for wikipedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from newapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login-user',loginuser,name="Login_user"),
    path("logout-user",logoutuser,name="Logout_user"),
    path("create-article",create_article,name="Create_Article"),
    path("read-articles",read_articles,name="read_articles"),
    path("view-article/<int:id>",view_article,name="View_article"),
    path('', view_all_articles, name='all_article_list'),
    path('login-form', show_login, name='show_login_form'),
    path('create-article-page', create_article_page, name='create_articles'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)