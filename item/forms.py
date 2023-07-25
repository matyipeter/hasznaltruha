from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Termék neve',
        'class': 'rounded-xl p-3',
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Leírás: méret, szín, állapot stb..',
        'class': 'rounded-xl p-3 w-full',
    }))

    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder':'Termék ára',
        'class': 'rounded-xl p-3',
    }))

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Termék neve',
        'class': 'rounded-xl p-3',
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Leírás: méret, szín, állapot stb..',
        'class': 'rounded-xl p-3 w-full',
    }))

    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder':'Termék ára',
        'class': 'rounded-xl p-3',
    }))