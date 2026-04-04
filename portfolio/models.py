from django.db import models

# Create your models here.
class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    ects_totais = models.IntegerField(default=180)
    link_site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=20, help_text="Número de docente") 
    email = models.EmailField(blank=True, null=True)
    link_lusofona = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    imagem = models.ImageField(upload_to='ucs/')
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    professores = models.ManyToManyField(Professor, related_name='ucs')

    def __str__(self):
        return f'{self.nome} ({self.ano}º Ano)'