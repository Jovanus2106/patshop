from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Toko
from .forms import TokoForm


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
