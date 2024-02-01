from django import forms


class ProductForm(forms.Form): # Товар
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    description_product = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Описание товара"}))
    store = forms.IntegerField()
    date_receipt = forms.DateTimeField(auto_now_add=True)
    image = forms.ImageField(widget=forms.FileInput(attrs={"placeholder": "Картинка товара"}))


class ChoiceProductById(forms.Form):  # id Товара
    id_product = forms.IntegerField()


class ChoiceProductByClientBydays(forms.Form):  # User
    id_client = forms.IntegerField()
    days = forms.IntegerField()
