from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'NamaAplikasi': 'PAT Shop',
        'Nama': 'Jovanus Irwan Susanto',
        'Kelas': 'PBP B',
    }
    return render(request, "main.html", context)

