from django.forms import ModelForm
from main.models import Toko

class TokoForm(ModelForm):
    class Meta:
        model = Toko 
        fields = ["name","price","category", "thumbnail","description","stock", "is_featured"]

        