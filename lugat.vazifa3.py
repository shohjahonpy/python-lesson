# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:39:22 2026

@author: Shohjaxon
"""

python_izohli_lugati={
    'integer':'Butun son',
    'float':'O\'nlik son',
    'string':"Matn",
    'list':'royxat',
    'tuple':"O'zgarmas ro'yxat"
    }
kalit=input('Kalit soz kiritng:').lower()
print(python_izohli_lugati.get(kalit,'Bunday kalit soz mavjud emas'))
tarjima=python_izohli_lugati.get(kalit)
if tarjima==None:
    print('Bunday kalit soz mavjud emas')
else:
    print(f"{kalit.title()} so'z {tarjima} deb tarjima qilinadi" )