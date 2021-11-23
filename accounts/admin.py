from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile
from .forms import ProfileCreationForm

class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    model = Profile
    fieldsets = UserAdmin.fieldsets
    add_fields = ((None,{'fields':('username','email','password1','password2','phone_number','address','city')}),)

admin.site.register(Profile, ProfileAdmin)