# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class Secondclass(models.Model):
#     id = models.IntegerField(primary_key=True)
#     secondclass = models.CharField(db_column='secondClass', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     first = models.ForeignKey('TFirst', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'secondclass'
#
#
# class TAddress(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20, blank=True, null=True)
#     detailaddress = models.CharField(db_column='detailAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     code = models.CharField(max_length=5, blank=True, null=True)
#     telephone = models.CharField(max_length=10, blank=True, null=True)
#     cellphone = models.CharField(max_length=11, blank=True, null=True)
#     user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_address'
#
#
# class TBooks(models.Model):
#     id = models.IntegerField(primary_key=True)
#     bookname = models.CharField(max_length=20, blank=True, null=True)
#     author = models.CharField(max_length=20, blank=True, null=True)
#     publishcom = models.CharField(db_column='publishCom', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     plushtime = models.DateTimeField(db_column='plushTime', blank=True, null=True)  # Field name made lowercase.
#     edition = models.IntegerField(blank=True, null=True)
#     impression = models.IntegerField(blank=True, null=True)
#     isbn = models.IntegerField(db_column='ISBN', blank=True, null=True)  # Field name made lowercase.
#     wordcount = models.IntegerField(db_column='wordCount', blank=True, null=True)  # Field name made lowercase.
#     numberpage = models.IntegerField(db_column='numberPage', blank=True, null=True)  # Field name made lowercase.
#     largebook = models.CharField(db_column='largeBook', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     paper = models.CharField(max_length=20, blank=True, null=True)
#     package = models.CharField(max_length=20, blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
#     dangprice = models.DecimalField(db_column='dangPrice', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     recomend = models.CharField(max_length=2000, blank=True, null=True)
#     briefintroduce = models.CharField(db_column='briefIntroduce', max_length=2000, blank=True, null=True)  # Field name made lowercase.
#     authorintroduce = models.CharField(db_column='authorIntroduce', max_length=2000, blank=True, null=True)  # Field name made lowercase.
#     catalog = models.CharField(max_length=2000, blank=True, null=True)
#     second = models.ForeignKey(Secondclass, models.DO_NOTHING, blank=True, null=True)
#     scor = models.IntegerField(blank=True, null=True)
#     envelope = models.CharField(max_length=100, blank=True, null=True)
#     sell_hot = models.IntegerField(blank=True, null=True)
#     last_display = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_books'
#
#
# class TFirst(models.Model):
#     id = models.IntegerField(primary_key=True)
#     parentclass = models.CharField(db_column='parentClass', max_length=20, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 't_first'
#
#
# class TOrder(models.Model):
#     id = models.IntegerField(primary_key=True)
#     total_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
#     order_uuid = models.CharField(max_length=20, blank=True, null=True)
#     user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
#     address = models.ForeignKey(TAddress, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_order'
#
#
# class TUser(models.Model):
#     id = models.IntegerField(primary_key=True)
#     nicname = models.CharField(max_length=20, blank=True, null=True)
#     password = models.CharField(max_length=20, blank=True, null=True)
#     logintime = models.DateTimeField(db_column='loginTime', blank=True, null=True)  # Field name made lowercase.
#     outtime = models.DateTimeField(db_column='outTime', blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_user'
#
#
# class TUserOrder(models.Model):
#     id = models.IntegerField(primary_key=True)
#     price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     amount = models.IntegerField(blank=True, null=True)
#     book = models.ForeignKey(TBooks, models.DO_NOTHING, blank=True, null=True)
#     order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_user_order'
