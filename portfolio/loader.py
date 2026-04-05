from portfolio.models import TFC
import json


TFC.objects.all().delete()

with open('portfolio/json/tfcs_2024_2025.json', encoding='utf-8') as f:
    tfcs = json.load(f)
    
    for item in tfcs:
        TFC.objects.create(
            titulo = item['titulo'],
            autores = item['autores'],
            orientador = item.get('orientadores', ''),
            resumo = item['sumario'],
            ano = item.get('ano', 2025),
            link_documento = item.get('link_pdf', ''),
            destaque = item.get('destaque', False)
        )

print(f"Foram carregados {len(tfcs)} TFCs com sucesso!")