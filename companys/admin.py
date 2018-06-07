from django.contrib import admin
from companys.models import Companys, Photo, Album
from companys.models import Pay

# Register your models here.

class CompanysAdmin(admin.ModelAdmin):
    list_display  = ('company_name', 'occ', 'location', 'scale', 'payment', 'owner')
    # list_filter   = ('modify_date',)
    search_fields = ('company_name', 'location')
    # prepopulated_fields = {'slug': ('title',)}


class PayAdmin(admin.ModelAdmin):
    list_display  = ('company_name', 'mem_num', 'g_pay')

admin.site.register(Companys, CompanysAdmin)
admin.site.register(Photo)
admin.site.register(Album)
admin.site.register(Pay, PayAdmin)
