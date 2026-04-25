from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    
    # Campos opcionais (null=True, blank=True permite que fiquem vazios)
    email = models.EmailField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True, help_text="Link para o perfil do LinkedIn ou da página da Lusófona")
    
    foto = models.ImageField(upload_to='professores/', null=True, blank=True)
    
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.titulo:
            return f"{self.titulo} {self.nome}"
        return self.nome