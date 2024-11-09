from django.contrib import admin
from .models import Academia, Assinantes


@admin.register(Academia)
class AcademiaAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Assinantes)
class AssinantesAdmin(admin.ModelAdmin):
    list_display = ['nome', 'academia']