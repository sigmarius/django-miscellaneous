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
    context = {
        'posts': posts,
        'menu': menu,
        'title': "Main page"
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


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')
