from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ProfileCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('username', 'email', 'phone_number', 'address', 'city')