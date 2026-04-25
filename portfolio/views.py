from django.shortcuts import render
from .models import Tecnologia 
from .models import Licenciatura, Formacao
from .models import Tecnologia, Licenciatura, Formacao, MakingOf 
from .models import Projeto
from .models import Competencia 

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tecnologia

from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto

from django.shortcuts import render, redirect, get_object_or_404
from .models import Licenciatura, Formacao


def home_view(request):
    return render(request, 'portfolio/home.html')


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all() 
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})


def percurso_view(request):
    licenciaturas = Licenciatura.objects.all()
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/percurso.html', {
        'licenciaturas': licenciaturas,
        'formacoes': formacoes
    })


def makingofs_view(request):
    makingofs = MakingOf.objects.all().order_by('-id') 
    return render(request, 'portfolio/makingofs.html', {'makingofs': makingofs})


def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def contactos_view(request):
    return render(request, 'portfolio/contactos.html')


def competencias_view(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        nivel = request.POST.get('nivel')
        Competencia.objects.create(nome=nome, nivel=nivel)
        return redirect('competencias')
        
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})




def tecnologias_view(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        Tecnologia.objects.create(nome=nome)
        return redirect('tecnologias')
    
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def eliminar_tecnologia(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    tecnologia.delete()
    return redirect('tecnologias')

def editar_tecnologia(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == "POST":
        tecnologia.nome = request.POST.get('nome')
        tecnologia.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/editar_tecnologia.html', {'tecnologia': tecnologia})




def projetos_view(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        Projeto.objects.create(nome=nome, descricao=descricao)
        return redirect('projetos')
    
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def eliminar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    projeto.delete()
    return redirect('projetos')

def editar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == "POST":
        projeto.nome = request.POST.get('nome')
        projeto.descricao = request.POST.get('descricao')
        projeto.save()
        return redirect('projetos')
    return render(request, 'portfolio/editar_projeto.html', {'projeto': projeto})




def eliminar_licenciatura(request, id):
    licenciatura = get_object_or_404(Licenciatura, id=id)
    licenciatura.delete()
    return redirect('percurso')

def eliminar_formacao(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    formacao.delete()
    return redirect('percurso')

def editar_licenciatura(request, id):
    licenciatura = get_object_or_404(Licenciatura, id=id)
    if request.method == "POST":
        licenciatura.nome = request.POST.get('nome')
        licenciatura.descricao = request.POST.get('descricao')
        licenciatura.save()
        return redirect('percurso')
    return render(request, 'portfolio/editar_licenciatura.html', {'licenciatura': licenciatura})