from django.contrib import admin
from .models import Professor

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    
    search_fields = ('nome', 'email')

    fieldsets = (
        ('Identificação Profissional', {
            'fields': ('nome', 'foto', 'bio')
        }),
        ('Contactos e Redes Sociais', {
            'fields': ('email', 'linkedin'),
        }),
    )

admin.site.register(Professor, ProfessorAdmin)