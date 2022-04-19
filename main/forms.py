from django import forms

from .models import AdUser


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')

    class Meta:
        model = AdUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')
