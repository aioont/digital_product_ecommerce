from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email id'}))
    msg_subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message subject'}))
    msg_content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mee content'}))
    class Meta:
        
        model = Contact
        fields = ('full_name', 'mail', 'msg_subject', 'msg_content')