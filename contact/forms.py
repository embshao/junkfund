from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='', min_length=4, max_length=150, 
                widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    business_name = forms.CharField(label='', min_length=4, max_length=150, 
                widget=forms.TextInput(attrs={'placeholder': 'Business name'}))
    email = forms.EmailField(required=True, label='',
                widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    class Meta:
        model = Contact
        fields = ('name', 'business_name', 'email')