from django.contrib import admin
from .models import CraftPost, Comment, Persona

# Register your models here.

admin.site.register(Persona)
admin.site.register(CraftPost)
admin.site.register(Comment)
