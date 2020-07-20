"""blog_project URL Configuration

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
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from blog.views.post import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('allauth.urls')),
    path('user/', include('blog.urls.user')),
    path('articles/', include('blog.urls.post')),
    path('', view=index, name="index"),
    path('about/', view=about, name="about"),
    path('contact/', include('contact.urls')),
    # path('about/', TemplateView.as_view(template_name="about.html")),
    # path('', TemplateView.as_view(template_name="index.html")),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import  TemplateView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('auth/', include('allauth.urls')),
#     path('user/', include('blog.urls.user')),
#     path('', TemplateView.as_view(template_name="index.html"))

# ]
