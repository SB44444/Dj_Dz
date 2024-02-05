 **Урок 1. Фреймворк Django. Введение в Django**  
*Задания 8*  
  
📌Создайте пару представлений в вашем первом приложении:
главная и о себе.  
📌 Внутри каждого представления должна быть переменная
html - многострочный текст с HTML вёрсткой и данными о
вашем первом Django сайте и о вас.  
📌 *Сохраняйте в логи данные о посещении страниц  
Реализация:  
<https://github.com/SB44444/Dj_Dz.git>  
  
**Урок 2.**  
*Домашнее задание*
Задание №8  
📌 Создайте три модели Django: клиент, товар и заказ.  
Клиент может иметь несколько заказов.  
Заказ может содержать несколько товаров.  
Товар может входить в несколько заказов.  
  
📌 Поля модели "Клиент":
○ имя клиента
○ электронная почта клиента
○ номер телефона клиента
○ адрес клиента
○ дата регистрации клиента  
  
📌 Поля модели "Товар":
○ название товара
○ описание товара
○ цена товара
○ количество товара
○ дата добавления товара  

📌 Поля модели "Заказ":  
○ связь с моделью "Клиент", указывает на клиента, сделавшего заказ  
○ связь с моделью "Товар", указывает на товары, входящие в заказ  
○ общая сумма заказа  
○ дата оформления заказа  
📌 *Допишите несколько функций CRUD для работы с моделями по желанию.  
Что по вашему мнению актуально в такой базе данных.
Реализация:  

<https://github.com/SB44444/Dj_Dz/tree/master/dj_dz/dz_app/dz_app2>  

**Урок 3.**  
*Домашнее задание.*  
Задание №7  
📌 Доработаем задачу 8 из прошлого семинара про клиентов,
товары и заказы.
📌 Создайте шаблон для вывода всех заказов клиента и
списком товаров внутри каждого заказа.
📌 Подготовьте необходимый маршрут и представление.  
  
_Задание №8*_  
📌 Продолжаем работать с товарами и заказами.  
📌 Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:  
○ за последние 7 дней (неделю)  
○ за последние 30 дней (месяц)  
○ за последние 365 дней (год)  
📌 *Товары в списке не должны повторятся  

Реализация:  

<https://github.com/SB44444/Dj_Dz/tree/master/dj_dz/dz_app/dz_app3>  
Django DZ_4 had been dane

**Урок 4.**  
*Домашнее задание.*  
Задание №6  
📌 Доработаем задачу про клиентов, заказы и товары из прошлого семинара.  
📌 Создайте форму для редактирования товаров в базе данных.  
  
📌 Измените модель продукта, добавьте поле для хранения фотографии продукта.  
📌 Создайте форму, которая позволит сохранять фото.  

Реализация:  

<https://github.com/SB44444/Dj_Dz/DZ4>  










