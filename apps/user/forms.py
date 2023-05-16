from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MatiCoffeeUser, Friend

class MatiCoffeeUserCreationForm(UserCreationForm):
    friend_code = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Código de amigos'}))

    class Meta(UserCreationForm.Meta):
        model = MatiCoffeeUser
        fields = ['username','password1','password2','friend_code']

class MatiCoffeeUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = MatiCoffeeUser
        fields = ['username','profile_img']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre...'}),
        }

class AvatarForm(forms.ModelForm):
    class Meta:
        model = MatiCoffeeUser
        fields = ['profile_img']


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = '__all__'
