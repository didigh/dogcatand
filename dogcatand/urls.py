"""dogcatand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import pet.views
import petphoto.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', pet.views.start, name = "start"),
    path('home/', pet.views.home, name = "home"),
    path('about/', pet.views.about, name = "about"),
    path('professional/', pet.views.professional, name = "professional"),
    path('portfolio/', petphoto.views.portfolio, name = "portfolio"),
    path('<int:blog_id>/detail', pet.views.detail, name = "detail"),
    # path('create', pet.views.create, name= "create"),
    path('new', pet.views.new, name= "new"),
    path('<int:blog_id>/edit', pet.views.edit, name = "edit"),
    path('<int:blog_id>/delete', pet.views.delete, name = "delete"),
    path('<int:blog_id>/comment/comment_create', pet.views.comment_create,name="comment_create"),
    path('<int:blog_id>/comment/<int:comment_id>/delete', pet.views.comment_delete, name="comment_delete"),
    path('<int:blog_id>/comment/<int:comment_id>/replay_create',pet.views.replay_create,name="replay_create"),
    path('<int:blog_id>/comment/<int:comment_id>/<int:re_id>/replay_delete', pet.views.replay_delete, name="replay_delete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
