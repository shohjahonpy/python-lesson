n_people=int(input('Bugun necha kishi bilan suhbat qildingiz?>> '))
ismlar=[]
for n in range(n_people):
    ismlar.append(input(f'{n+1} - suhbat qilgan odamingiz kim- '))
print(ismlar)    