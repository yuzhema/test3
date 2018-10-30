from django.db import models

# Create your models here.
from admins_app.models import User
from home_page.models import Books


class Address(models.Model):
    name = models.CharField(max_length=20)
    detail_address = models.CharField(max_length=200)  # Field name made lowercase.
    zipcode = models.CharField(max_length=6)
    telephone = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=11)
    users = models.ForeignKey(to=User,on_delete=models.CASCADE,db_column='user_idd')

    class Meta:
        db_table = 't_address'


class Order(models.Model):
    create_date=models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    order_uuid = models.CharField(max_length=20)

    status=models.BooleanField()
    user= models.ForeignKey(to=User,on_delete=models.CASCADE,db_column='order_uid')
    address = models.ForeignKey(to=Address,on_delete=models.CASCADE,db_column='order_addid')

    class Meta:
        db_table = 't_order'


class UserOrder(models.Model):


    amount = models.IntegerField()
    total_price=models.IntegerField()
    book = models.ForeignKey(to=Books,on_delete=models.CASCADE,db_column='book_id')
    order = models.ForeignKey(to=Order,on_delete=models.CASCADE,db_column='order_id')

    class Meta:

        db_table = 't_user_order'
