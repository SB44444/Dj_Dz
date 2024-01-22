# from django.shortcuts import render

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('main get request')
    html = ('<!DOCTYPE html>'
            '<html lang="en">'
            '<head>'
            '<meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            '<title>Main</title>'
            '</head>'
            '<body>'
            '<h1>Главная</h1>'
            '<h2>Старт проекта интернет-мазина</h2>'
            '<footer>'
            '<hr>'
            '<H6>Расзрешено свободное использоание материалов сайта</H6>'
            '</footer>'
            '</body>'
            '</html>')

    return HttpResponse(html)


def about(request):
    logger.info('about get request')
    html = ('<!DOCTYPE html>'
            '<html lang="en">'
            '<head>'
            '<meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            '<title>About</title>'
            '</head>'
            '<body>'
            '<h1>Обо мне</h1>'
            '<h2>Об авторе интернет-мазина</h2>'
            '<footer>'
            '<hr>'
            '<a href=''>Вернуться на главную страницу</a>'
            '<H6>Расзрешено свободное использоание материалов сайта</H6>'
            '</footer>'
            '</body>'
            '</html>')

    return HttpResponse(html)
