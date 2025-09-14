from django.urls import path
from .views import  show_main, detail_product, add_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add/', add_product, name='add_product'),
    path('detail/<str:id>/', detail_product, name='detail_product'),

]

