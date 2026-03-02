# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:19:20 2026

@author: Shohjaxon
"""

menu={'osh':40000,
         'salat':10000,
         'non':5000,
         'shashlik':25000,
         'suzma':8000,
         'somsa':35000,
         'shorva':20000,
         'choy':3000,
         'cola':15000
    }
print('3 ta taom buyurtma bering')
buyurtmalar=[]
for n in range(3):
    buyurtmalar.append(input(f'{n+1}- taom:').lower())
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f'{buyurtma.title()} {menu[buyurtma]} so\'m')
    else:
        print(f'kechirasiz bizda {buyurtma} mavjud emas')
    
