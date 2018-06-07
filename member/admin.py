from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import SignupForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('추가 정보', {'fields': ('user_categ', 'full_name','img_profile', 'gender', 'birth_date', 'profile', 'phone_number', 'job_selects1', 'job_selects2', 'job_selects3')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('추가 정보', {
            'fields': ('user_categ','full_name','img_profile', 'gender', 'birth_date', 'profile', 'phone_number', 'job_selects1', 'job_selects2', 'job_selects3'),
        }),
    )
    add_form = SignupForm


admin.site.register(User, UserAdmin)
