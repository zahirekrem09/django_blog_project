from django.urls import path

from blog.views.user import retrieve, updateUser

urlpatterns = [
    path('<str:username>/', view=retrieve, name="retrieve"),
    path('<str:username>/updateprofile/',
         view=updateUser, name="updateprofile"),
    # path('<str:username>/user-upload-photo/',
    # view=user_upload_photo, name="user-upload-photo"),
]
