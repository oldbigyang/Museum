from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Artifact, CustomUser 

# Register your models here.

admin.site.register(Artifact)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('real_name', 'id_card_number', 'phone_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
