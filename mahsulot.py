bozorliklar=int(input('Dokondan nechta narsa xarid qildingiz>>'))
mahsulot=[]
narxi=[]
for n in range(bozorliklar):
    mahsulot.append(input(f'{n+1}- mahsulotingiz nomi? '))
    narxi.append(int(input(f'{n+1} - mahsulot narxi? ')))
print(mahsulot)
print(narxi)
print('sizning jami xaridingiz narxi:' ,sum(narxi))

    
