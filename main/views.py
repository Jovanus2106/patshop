from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Toko
from .forms import TokoForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm #registrasi
from django.contrib import messages #registrasi
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.http import JsonResponse


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
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'categories': Toko.CATEGORY_CHOICES 
    }
    return render(request, "main.html",context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login_user'))
    messages.success(request, "Kamu sudah logout")
    response.delete_cookie('last_login')
    return response

def edit_produk(request, id):
    produk = get_object_or_404(Toko, pk=id)
    form = TokoForm(request.POST or None, instance=produk)
    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.success(request,"Produk berhasil diubah")
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_produk.html", context)

@csrf_exempt
@require_POST
def add_products_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price= request.POST.get("price")
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    stock= request.POST.get("stock")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_toko = Toko(
        name=name, 
        price=price,
        description=description,
        thumbnail=thumbnail,
        category=category,
        stock=stock,
        is_featured=is_featured,
        user=user
    )
    new_toko.save()

    return HttpResponse(b"CREATED", status=201)

def delete_produk(request, id):
    produk = get_object_or_404(Toko, pk=id)
    produk.delete()
    messages.success(request, "Produk telah dihapus")
    return HttpResponseRedirect(reverse('main:show_main'))

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Selamat Anda berhasil Login ')
            response_data = {
                'success': True,
                'message': 'Login berhasil! Selamat datang kembali 👋',
                'redirect_url': reverse('main:show_main')
            }
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse(response_data)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            errors = form.errors.as_json()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Username atau password salah!'}, status=400)
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Account created successfully!',
                    'redirect_url': reverse('main:login_user')
                })
            return redirect('main:login_user')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'message': 'Registration failed. Please check your input.'
                }, status=400)
    return render(request, 'register.html', {'form': form})

@login_required(login_url='/login')
def detail_product(request, id):
    return render(request, "detail.html", {"product_id": id})

# Tambah produk
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
    data = [
        {
            'id': str(toko.id),
            'name': toko.name,
            'price': toko.price,
            'description': toko.category,
            'thumbnail': toko.thumbnail,
            'category': toko.category,
            'is_featured': toko.is_featured,
            'stock': toko.stock,
            'user_id': toko.user_id,
        }
        for toko in Toko_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, Toko_id):
   Toko_item = Toko.objects.filter(pk=Toko_id)
   xml_data = serializers.serialize("xml", Toko_item)
   return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, Toko_id ):
    try:
        toko = Toko.objects.select_related('user').get(pk=Toko_id)
        data = {
            'id': str(toko.id),
            'name': toko.name,
            'price': toko.price,
            'description': toko.category,
            'thumbnail': toko.thumbnail,
            'category': toko.category,
            'is_featured': toko.is_featured,
            'stock': toko.stock,
            'user_id': toko.user_id,
            'user_username': toko.user.username if toko.user_id else None,
        }
        return JsonResponse(data)
    except Toko.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
