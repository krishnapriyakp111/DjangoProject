from django.db import models

# Create your models here.


class services:
    title: str
    des: str
    img: str


class Service(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=230)
    img=models.ImageField(upload_to='pics')
