from django.db import models
from adminpanel.models import product,product_img

class user_register(models.Model):
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(max_length=50)
    mobile = models.IntegerField(max_length=20)
    password = models.CharField(max_length=20)

    @staticmethod
    def customar_chack(c):
        try:
            return user_register.objects.get(username = c)
        except:
            return False
    
class wishlist(models.Model):
    product_id = models.ForeignKey(product,on_delete=models.SET_NULL,blank=True,null=True)
    customer_id = models.ForeignKey(user_register, on_delete=models.SET_NULL,blank=True,null=True)
    wish_date = models.DateField(auto_now=True)





