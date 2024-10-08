from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='user',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='password',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
