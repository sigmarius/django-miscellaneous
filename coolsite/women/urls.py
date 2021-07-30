from django.urls import path, re_path

from .views import *

urlpatterns = [
    # http://127.0.0.1:8080/
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpost/', addpost, name='add_post'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')
]
