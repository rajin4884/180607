from django.contrib import admin
from .models import Code_categ, Code


class Code_categAdmin(admin.ModelAdmin):
    list_display  = ('pk','cc_name')
    list_filter   = ('cc_name',)
    search_fields = ('pk','cc_name')

class CodeAdmin(admin.ModelAdmin):
    list_display  = ('category','c_num','c_name')
    list_filter   = ('category','c_num','c_name')
    search_fields = ('category','c_num','c_name')

admin.site.register(Code_categ, Code_categAdmin)
admin.site.register(Code,CodeAdmin)
