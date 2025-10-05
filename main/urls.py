from django.urls import path
from .views import  show_main, detail_product, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id
app_name = 'main'
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_produk
from main.views import delete_produk
from main.views import add_products_entry_ajax


urlpatterns = [
    path('', show_main, name='show_main'),
    path('add/', add_product, name='add_product'),
    path('detail/<str:id>/', detail_product, name='detail_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:Toko_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:Toko_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('produk/<uuid:id>/edit', edit_produk, name='edit_produk'),
    path('produk/<uuid:id>/delete', delete_produk, name='delete_produk'),
    path('add-products-ajax', add_products_entry_ajax, name='add_products_entry_ajax'),
]

