# forms.py
from django import forms
from .models import Hobies
 
class HotelForm(forms.ModelForm):
 
    class Meta:
        model = Hobies
        fields = ['title', 'image','description', 'is_showed','kategori']