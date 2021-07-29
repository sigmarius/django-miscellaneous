from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': 'About our site', 'url_name': 'about'},
        {'title': 'Add post', 'url_name': 'add_post'},
        {'title': 'Contact', 'url_mane': 'contact'},
        {'title': 'Login', 'url_name': 'login'},
        ]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'cats': cats,
        'title': "Main page",
        'cat_selected': 0,
    }
    print(context['menu'])
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': "About our site"})


def addpost(request):
    return HttpResponse('Adding post')


def contact(request):
    return HttpResponse('Contact us')


def login(request):
    return HttpResponse('Please login')


def show_post(request, post_id):
    return HttpResponse(f'Showing page with id = {post_id}')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'cats': cats,
        'title': "Categories page",
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')
