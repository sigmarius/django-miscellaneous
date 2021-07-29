from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8080/
    path('about/', about, name='about'),
    path('addpost/', addpost, name='add_post'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')
]
