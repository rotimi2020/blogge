from django import forms
from .models import Contact, Blog_Post

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        error_messages={'required': 'Enter your full name.'}
    )

    email = forms.EmailField(
        required=True,
        error_messages={'required': 'Enter your valid Email.'}
    )

    message = forms.CharField(
        required=True,
        error_messages={'required': 'Meassage Required !'}
    )    

    is_clicked = forms.BooleanField(
        required=True,
        error_messages={'required': 'You must agree before sending the message.'}
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'is_clicked']
