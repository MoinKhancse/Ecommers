from django.db import models
from django.contrib.auth.models import AbstractUser

class usertype(models.Model):
    type_name = models.CharField(max_length=100)

class User(AbstractUser):
    user_type = models.ForeignKey(usertype,on_delete=models.CASCADE,default = 1)
 
class category(models.Model):
    category_name = models.CharField(max_length=100)
    category_img = models.ImageField(upload_to='category/',blank=True,null=True,default=None)

class product(models.Model):
    peoduct_name = models.CharField(max_length=100)
    product_old_price = models.FloatField()
    product_new_price = models.FloatField()
    product_category = models.ForeignKey(category,on_delete=models.CASCADE,default=1,related_name='cat')


class product_img(models.Model):
    product_image_all = models.ImageField(upload_to='product/',blank=True,null=True)
    product_table = models.ForeignKey(product,on_delete=models.CASCADE, related_name='prod')