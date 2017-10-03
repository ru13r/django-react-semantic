from django.contrib import admin
from .models import DRFTest
# Register your models here.

class DRFTestAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(DRFTest, DRFTestAdmin)