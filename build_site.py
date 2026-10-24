# Genera index.html para la página en internet a partir de la versión de Claude.
import shutil, os
SRC='/home/claude/elite-web/index.html'; REPO='/home/claude/elitefood'
h=open(SRC).read()
head='''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Elite Food Distributor: Latin snacks, juices and candy distribution. Bemar Snacks, La Molienda, Pelly, Petit.">
<link rel="icon" href="img/logo-elite.jpg">
<style>html,body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
'''
i=h.index('</style>')+len('</style>')
doc=(head+h[:i]+'\n</head>\n<body>\n'+h[i:]+'\n</body>\n</html>\n').replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
old='<div class="hero-cta"><a class="btn btn-gold" href="#productos">'
k=doc.rindex(old); j=doc.index('</div>',k)
new='<div class="hero-cta"><a class="btn btn-gold" href="#productos"><span class="es">Ver productos</span><span class="en">See products</span></a><a class="btn btn-line" href="catalogo-elite-food.pdf" target="_blank" rel="noopener"><span class="es">Catálogo PDF (Español)</span><span class="en">PDF Catalog (Spanish)</span></a><a class="btn btn-line" href="catalog-elite-food-en.pdf" target="_blank" rel="noopener"><span class="es">Catálogo PDF (Inglés)</span><span class="en">PDF Catalog (English)</span></a></div>'
doc=doc[:k]+new+doc[j+6:]
open(os.path.join(REPO,'index.html'),'w').write(doc)
shutil.rmtree(os.path.join(REPO,'img'),ignore_errors=True); os.makedirs(os.path.join(REPO,'img'))
import re
for f in sorted(set(re.findall(r'img/([A-Za-z0-9._-]+)',doc))|set(re.findall(r'"([A-Za-z0-9_-]+\.webp)"',doc))):
    shutil.copy(os.path.join('/home/claude/elite-web/img',f),os.path.join(REPO,'img',f))
shutil.copy('/home/claude/catalogo/Catalogo-Elite-Food.pdf',os.path.join(REPO,'catalogo-elite-food.pdf'))
shutil.copy('/home/claude/catalogo/Catalog-Elite-Food-EN.pdf',os.path.join(REPO,'catalog-elite-food-en.pdf'))
print('ok', len(os.listdir(os.path.join(REPO,'img'))),'images')
