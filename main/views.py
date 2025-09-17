from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Toko
from .forms import TokoForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products = Toko.objects.all()
    else:
        products = Toko.objects.filter(user=request.user)

    context = {
        'NamaAplikasi': 'PAT Shop',
        'Nama': request.user.username,
        'Kelas': 'PBP B',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/login')
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

def add_product(request):
    form = TokoForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        Toko_entry = form.save(commit = False)
        Toko_entry.user = request.user
        Toko_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "add_product.html", context)

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

