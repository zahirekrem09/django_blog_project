
from django.urls import path, include
from blog.views.post import BlogPageView
from blog.views.article import dashboard, addarticle, updateArticle, deleteArticle, addComment, detail
urlpatterns = [
    #path('', view=articles, name="articles"),
    path('', BlogPageView.as_view(), name='articles'),
    #path('post/<int:id>', BlogDetailView.as_view(), name='post'),
    path('post/<int:id>', view=detail, name='post'),
    path('dashboard/', view=dashboard, name="dashboard"),
    path('addarticle/', view=addarticle, name="addarticle"),
    path('update/<int:id>', view=updateArticle, name="update"),
    path('delete/<int:id>', view=deleteArticle, name="delete"),
    path('comment/<int:id>', view=addComment, name="comment"),
]


# urlpatterns = [
#     path('', views.articles, name="articles"),
#     path('dashboard/', views.dashboard, name="dashboard"),
#     path('addarticle/', views.addarticle, name="addarticle"),
#     path('article/<int:id>', views.detail, name="detail"),
#     path('update/<int:id>', views.updateArticle, name="update"),
#     path('delete/<int:id>', views.deleteArticle, name="delete"),
#     path('comment/<int:id>', views.addComment, name="comment"),
# ]
