from django.urls import path, re_path

from .views import *

urlpatterns = [
    # http://127.0.0.1:8080/
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category')
]
