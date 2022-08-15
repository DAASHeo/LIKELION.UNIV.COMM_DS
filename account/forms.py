from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class signupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1','nickname']