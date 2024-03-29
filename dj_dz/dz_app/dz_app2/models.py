from django.db import models


class User(models.Model):  # Клиент
    name = models.CharField(max_length=100)
    email = models.EmailField()
    adress = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    date_visit = models.DateTimeField(auto_now_add=True)
    about = models.TextField()

    def __str__(self):
        return (f'Клиент: {self.name}, почта: {self.email}, адрес: {self.adress}, телефон: {self.tel},/'
                f'дата_визита: {self.date_visit}, коментарии: {self.about}')


class Product(models.Model):  # Товар
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    date_receipt = models.DateTimeField(auto_now_add=True)
    store = models.IntegerField()

    def __str__(self):
        return (f'товар: {self.name}, цена: {self.price}, описание: {self.description},/'
                f'дата_прихода: {self.date_receipt}, количество: {self.store}')


class Order(models.Model):  # Заказ
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return (f'Клиент: {self.customer}, товар: {self.products},/'
                f'дата_заказа: {self.date_ordered}, сумма: {self.total_price}')  # Заказ: {self.id},
