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

class Tecnologia(models.Model):
    NIVEL_CHOICES = [(i, str(i)) for i in range(1, 6)]
    
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='tecnologias/')
    link_oficial = models.URLField()
    detalhes = models.TextField()
    nivel_interesse = models.IntegerField(choices=NIVEL_CHOICES)

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    CATEGORIA_CHOICES = [
        ('Soft', 'Soft Skill'),
        ('Hard', 'Hard Skill'),
    ]
    NIVEL_CHOICES = [
        ('Iniciante', 'Iniciante'),
        ('Intermédio', 'Intermédio'),
        ('Avançado', 'Avançado'),
    ]
    
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)

    def __str__(self):
        return f'{self.nome} ({self.nivel})'

class Formacao(models.Model):
    designacao = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    descricao = models.TextField()
    competencias_adquiridas = models.ManyToManyField(Competencia, blank=True, related_name='formacoes')

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return f'{self.designacao} - {self.instituicao}'

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    video_demo = models.URLField(blank=True, null=True)
    link_github = models.URLField(blank=True, null=True)
    
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.SET_NULL, null=True, blank=True, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    competencias = models.ManyToManyField(Competencia, blank=True, related_name='projetos')

    def __str__(self):
        return self.titulo