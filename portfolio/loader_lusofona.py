from portfolio.models import Licenciatura, UnidadeCurricular
import json


UnidadeCurricular.objects.all().delete()
Licenciatura.objects.all().delete()

with open('files/ULHT260-PT.json', encoding='utf-8') as f:
    curso_data = json.load(f)
    
    
    licenciatura = Licenciatura.objects.create(
        nome = curso_data.get('courseName', 'Ingformática de Gestão'),
        descricao = curso_data.get('presentation', ''),
        ects_totais = 180
    )
    
    
    ucs = curso_data.get('courseFlatPlan', [])
    
    for item in ucs:
        UnidadeCurricular.objects.create(
            nome = item['curricularUnitName'],
            licenciatura = licenciatura, # Liga a cadeira ao curso acabado de criar!
            ano = item.get('curricularYear', 1),
            semestre = item.get('semester', 1),
            ects = item.get('ects', 6)
        )

print(f"Foram carregadas a Licenciatura '{licenciatura.nome}' e {len(ucs)} UCs com sucesso!")