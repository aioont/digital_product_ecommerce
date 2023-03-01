from django import forms
from .models import ProviderMessage,AdminMessage



class ProviderMessageForm(forms.ModelForm):
    class Meta:
        model = ProviderMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your query about service ...'}),
        }

    def clean_subject(self):
        return "Query about service %s" % self.cleaned_data['subject']
    labels = {
            'subject': '',
        }
    widgets = {
            'subject': forms.HiddenInput(),
        }


class AdminMessageForm(forms.ModelForm):
    class Meta:
        model = AdminMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'readonly': True}),
            'email': forms.EmailInput(attrs={'readonly': True}),
            'subject': forms.TextInput(),
            'message': forms.Textarea(attrs={'placeholder': 'Description message about service and attach your profile in any social media to prove authenticity of your service ...  Provide service provider name, contact, service title, description, expected cost of service. Also send mail to admin@dpe.com to add service provider image, service image, video'}),
        }

    def __init__(self, *args, **kwargs):
        super(AdminMessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['email'].required = False





