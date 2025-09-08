from django.db import models

class Product(models.Model):

    CATEGORY_CHOICES = [
    ('ELECTRONICS', 'Elektronik'),
    ('FASHION', 'Fashion'),
    ('HOME', 'Peralatan Rumah'),
    ('FOOD', 'Makanan & Minuman'),
    ('SPORTS', 'Olahraga')]


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('ELECTRONICS', 'Elektronik'),
        ('FASHION', 'Fashion'),
        ('HOME', 'Peralatan Rumah'),
        ('FOOD', 'Makanan & Minuman'),
        ('SPORTS', 'Olahraga'),
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    stock = models.IntegerField()

    
    def __str__(self):
        return self.name
    

