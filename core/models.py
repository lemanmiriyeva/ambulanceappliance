from django.db import models

# Create your models here.

class Quotes(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    zip_code=models.CharField(max_length=255)
    class Meta:
        verbose_name='Quote'
        verbose_name_plural='Quotes'
    
    

class About(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=255,null=True,blank=True)
    small_desc=models.CharField(max_length=255)
    large_desc=models.CharField(max_length=255)
    class Meta:
        verbose_name='About'
        verbose_name_plural='About'
        
    def __str__(self):
        return self.title

class Service(models.Model):
    image=models.ImageField()
    icon=models.ImageField()
    title=models.CharField(max_length=255,null=True,blank=True)
    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'

class Works(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=255)
    filter=models.CharField(max_length=255)
    class Meta:
        verbose_name='Work'
        verbose_name_plural='Works'

class Reviews(models.Model):
    full_name=models.CharField(max_length=255)
    stars=models.IntegerField()
    message=models.TextField()
    class Meta:
        verbose_name='Review'
        verbose_name_plural='Reviews'

class Subscribers(models.Model):
    email=models.EmailField()
    class Meta:
        verbose_name='Subscriber'
        verbose_name_plural='Subscribers'

class Contact(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    message=models.TextField()
    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contact'

    