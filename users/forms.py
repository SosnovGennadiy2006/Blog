from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.core.exceptions import ValidationError 
from django.forms.fields import EmailField 
from django.forms.forms import Form
from .models import Profile
from PIL import Image
import os
from django.conf import settings
 
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}

class ProfileChangeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']

class AvatarChangeForm(forms.ModelForm):
    avatar = forms.ImageField(required=True)
    x = forms.IntegerField(required=True)
    y = forms.IntegerField(required=True)
    width = forms.IntegerField(required=True)
    height = forms.IntegerField(required=True)
    
    class Meta:
        model = Profile
        fields = ['avatar']

    
    def save(self, instance):
        super(AvatarChangeForm, self).save()
        
        photo = self.cleaned_data.get('avatar')

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        image.close()
        resized_image.save(os.path.join(settings.MEDIA_ROOT, f'profile/user/{instance.user_id}.jpg'))