from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# link for class HttpRequest
def index(request):
    return HttpResponse("<h1>Page of application Women</h1>")


def categories(request, catid):
    if request.GET:
        print(request.GET)

    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Pages by their categories</h1><p>{catid}</p>")


def archive(request, year):
    if 2021 < int(year) < 2099:
        raise Http404()

    if int(year) > 2100:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')
