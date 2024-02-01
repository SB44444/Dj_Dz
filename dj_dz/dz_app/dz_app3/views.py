from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from dz_app3.models import User, Product, Order


def index(request):
    context = {'index': ['Старт проекта интернет-мазина']}

    # logger.info('main get request')
    return render(request, 'dz_app3/index.html', context=context)


def all_Users3_view(request):
    users = User.objects.all()
    context = '<br>'.join([str(users) for users in users])
    return render(request, 'dz_app3/all_users.html', context)
    # out_str = '<br>'.join([str(users) for users in users])
    # return HttpResponse(out_str)


def all_Products3_view(request):
    products = Product.objects.all()
    context = '<br>'.join([str(products) for products in products])
    return render(request, 'dz_app3/all_prducts.html', context)
    # out_str = '<br>'.join([str(products) for products in products])
    # return HttpResponse(out_str)


def user_Order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app3/all_user_order.html', {'user': user, 'order': orders})


def week_order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app3/week_user_orders.html', {'order': orders})


def month_order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app3/month_user_orders.html', {'order': orders})


def year_order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app3/year_user_orders.html', {'order': orders})


def user_order_in_year(request):
    users = User.objects.all()
    out_str = '<br>'.join([str(users) for users in users])
    return HttpResponse(out_str)
# __________________________________________________________________________________________________


def get_order_week(self):
    products = Order.objects.get(id=self.pk).products.all()
    if datetime.now().date() - self.date_ordered.day <= 7:
        return f'Заказ {self.date_ordered}: {", ".join([p.name for p in products])}'
    else:
        return 'За последнюю неделю заказов не было'


def get_order_month(self):
    products = Order.objects.get(id=self.pk).products.all()
    if datetime.now().date() - self.date_ordered.day <= 30:
        return f'Заказ {self.date_ordered}: {", ".join([p.name for p in products])}'
    else:
        return 'За последний месяц заказов не было'


def get_order_year(self):
    products = Order.objects.get(id=self.pk).products.all()
    if datetime.now().date() - self.date_ordered.day <= 365:
        return f'Заказ {self.date_ordered}: {", ".join([p.name for p in products])}'
    else:
        return 'За последний год заказов не было'
