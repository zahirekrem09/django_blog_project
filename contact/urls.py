from django.urls import path
from .views import emailView

urlpatterns = [
    path('', emailView, name='contact'),
]
