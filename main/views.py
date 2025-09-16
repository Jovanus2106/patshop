from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Toko
from .forms import TokoForm
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    products = Toko.objects.all()
    context = {
        'NamaAplikasi': 'PAT Shop',
        'Nama': 'Jovanus Irwan Susanto',
        'Kelas': 'PBP B',
        'products': products
    }
    return render(request, "main.html", context)


def detail_product(request, id):
    product = get_object_or_404(Toko, pk=id)
    return render(request, "detail.html", {"product": product})

# Tambah produk

def add_product(request):
    if request.method == "POST":
        form = TokoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:show_main")
    else:
        form = TokoForm()
    return render(request, "add_product.html", {"form": form})


def show_xml(request):
     Toko_list = Toko.objects.all()
     xml_data = serializers.serialize("xml", Toko_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    Toko_list = Toko.objects.all()
    json_data = serializers.serialize("json", Toko_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, Toko_id):
   Toko_item = Toko.objects.filter(pk=Toko_id)
   xml_data = serializers.serialize("xml", Toko_item)
   return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, Toko_id ):
   news_item = Toko.objects.get(pk=Toko_id)
   json_data = serializers.serialize("json", [news_item])
   return HttpResponse(json_data, content_type="application/json")

