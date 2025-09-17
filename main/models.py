from django.db import models
import  uuid
from django.contrib.auth.models import User

class Toko(models.Model):

    CATEGORY_CHOICES = [
    ('ELECTRONICS', 'Elektronik'),
    ('FASHION', 'Fashion'),
    ('HOME', 'Peralatan Rumah'),
    ('FOOD', 'Makanan & Minuman'),
    ('SPORTS', 'Olahraga')]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    stock = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.name
    

