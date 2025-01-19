from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, ContactsFormView, BlogDetailView, BlogDeleteView, BlogUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path("home/", BlogListView.as_view(), name="home"),
    path("add_articles/", BlogCreateView.as_view(), name="add_articles"),
    path("contacts/", ContactsFormView.as_view(), name="contacts"),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("add_article/", BlogCreateView.as_view(), name="add_article"),
    path("del_article/<int:pk>/", BlogDeleteView.as_view(), name="del_article"),
    path("update_article/<int:pk>/", BlogUpdateView.as_view(), name="update_article"),
]
