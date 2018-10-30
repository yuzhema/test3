
from django.db import models

# Create your models here.
from admins_app.models import User


class FirstCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_category = models.CharField(max_length=20)
    class Meta:
        db_table = 't_first'


class SecondCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    child_category=models.CharField(max_length=20)
    # first_cate_id = models.CharField(max_length=20)
    first = models.ForeignKey(to=FirstCategory,on_delete=models.CASCADE,db_column='first_cate_id')
    class Meta:
        db_table = 't_second'



class Books(models.Model):
    bookname = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    book_publish = models.CharField( max_length=20)
    publish_time = models.DateTimeField()
    revision = models.IntegerField()
    # press_count = models.IntegerField()
    isbn = models.IntegerField(db_column='ISBN')
    word_count = models.IntegerField()
    page_number = models.IntegerField()
    open_type = models.CharField( max_length=20)
    paper = models.CharField(max_length=20)
    package = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dang_price = models.DecimalField( max_digits=5, decimal_places=2)
    editor_recommend=models.BooleanField()
    content_introduce=models.CharField(max_length=2000)
    author_introduce=models.CharField(max_length=2000)
    menu=models.CharField(max_length=2000)
    media_review=models.IntegerField()
    digest_image_path=models.FileField(upload_to='pic1')
    produce_image_path=models.FileField(upload_to='pic2')
    printing_time=models.DateTimeField()
    stock=models.IntegerField()
    shelves_date=models.DateTimeField()
    customer_score = models.IntegerField()
    book_status=models.BooleanField()
    sales=models.IntegerField()
    second = models.ForeignKey(to=SecondCategory,on_delete=models.CASCADE,db_column='second_cate_id')
    class Meta:
        db_table = 't_books'









