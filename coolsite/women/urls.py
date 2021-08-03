from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    # http://127.0.0.1:8080/
    # path('', cache_page(60)(WomenHome.as_view()), name='home'),  # 60seconds cached
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category')
]
