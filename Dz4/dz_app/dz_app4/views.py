from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import User, Product, Order
from . forms import ImageForm, ProductForm, UserForm
import logging

logger = logging.getLogger(__name__)


def index(request):
    # return HttpResponse("Hello, world!")
    # logger.info('main get request')
    context = {'index': ['Старт проекта интернет-мазина 4']}
    return render(request, 'dz_app4/index.html', context=context)


def about(request):

    # logger.info('main get request')
    context = {'about': ['Страница о сайте 4']}
    return render(request, 'dz_app4/about.html', context=context)


def all_Products4_view(request):
    products = Product.objects.all()
    context = '<br>'.join([str(products) for products in products])
    return render(request, 'dz_app4/all_prducts.html', context)
    # out_str = '<br>'.join([str(products) for products in products])
    # return HttpResponse(out_str)


def user_4Order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app4/all_user_order.html', {'user': user, 'order': orders})


def week_4order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app4/week_user_orders.html', {'order': orders})


def month_4order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app4/month_user_orders.html', {'order': orders})


def year_4order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(client=user)
    return render(request, 'dz_app4/year_user_orders.html', {'order': orders})


def user_4order_in_year(request):
    users = User.objects.all()
    out_str = '<br>'.join([str(users) for users in users])
    return HttpResponse(out_str)


def update_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = 'Повторите ввод данных'
        if form.is_valid():
            product = form.cleaned_data['product']
            product_name = product.name
            updated_product = Product.objects.filter(name=product_name).first()

            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            date_receipt = form.cleaned_data['date_receipt']
            store = form.cleaned_data['store']

            updated_product.name = name
            updated_product.price = price
            updated_product.description = description
            updated_product.date_receipt = date_receipt
            updated_product.store = store
            updated_product.save()
            message = 'Данные успешно сохранены'
            logger.info(f"Обновлен подукт: {name}, цена:{price}, дата поступления:{date_receipt}, количество:{store}")
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'dz_app4/update_product.html', {'form': form, 'message': message})


def update_client(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Повторите ввод данных'
        if form.is_valid():
            client = form.cleaned_data['product']
            client_name = client.name
            updated_client = User.objects.filter(name=client_name).first()

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            adress = form.cleaned_data['adress']
            tel = form.cleaned_data['tel']
            date_visit = form.cleaned_data['date_visit']
            about_ = form.cleaned_data['about']

            updated_client.name = name
            updated_client.price = email
            updated_client.description = adress
            updated_client.date_receipt = tel
            updated_client.store = date_visit
            updated_client.about_ = about_
            updated_client.save()
            message = 'Данные успешно сохранены'
            logger.info(f"Измение данных:: {name}, телефон:{tel}, комментарии:{about_}")
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'dz_app4/update_product.html', {'form': form, 'message': message})


def upload_image(request, product_id):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product.objects.filter(pk=product_id).first()
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            product.image_field = fs.save(image.name, image)
            product.save()
            logger.info("Изображение успешно сохранено")
    else:
        form = ImageForm()
    return render(request, 'dz_app4/upload_image.html', {'form': form})
