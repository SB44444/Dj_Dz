# from django.shortcuts import render
from django.http import HttpResponse
from dz_app2.models import User, Product, Order


def index(request):
    # logger.info('main get request')
    html = ('<!DOCTYPE html>'
            '<html lang="en">'
            '<head>'
            '<meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            '<title>Main</title>'
            '</head>'
            '<body>'
            '<h1>Главная DZ 2</h1>'
            '<h2>Старт проекта интернет-мазина</h2>'
            '<footer>'
            '<hr>'
            '<H6>Расзрешено свободное использоание материалов сайта</H6>'
            '</footer>'
            '</body>'
            '</html>')

    return HttpResponse(html)


def all_Users2_view(request):
    users = User.objects.all()
    out_str = '<br>'.join([str(users) for users in users])
    return HttpResponse(out_str)


def all_Products2_view(request):
    products = Product.objects.all()
    out_str = '<br>'.join([str(products) for products in products])
    return HttpResponse(out_str)


