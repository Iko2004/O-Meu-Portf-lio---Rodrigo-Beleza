from django.contrib import admin

from .models import (
    Licenciatura, Professor
)

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ects_totais')
    search_fields = ('nome', 'descricao')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero', 'email')
    search_fields = ('nome', 'numero', 'email')