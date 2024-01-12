from math import * #неправильный порядок
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #изменить переменную
S=a**2
print("Ruudu pindala", round(S,2)) #округлить
P=4*a
print("Ruudu ümbermõõt", round(P,2)) #ковычки/округлить
di=a*sqrt(2) #math не нужен/ sqr поменять на sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #лишняя скобка
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #добавить float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #добавить float
S=b*c
print("Ristküliku pindala", round(S,2)) #добавить ковычки/округлить
P=2*(b+c)#знак умножения
print("Ristküliku ümbermõõt", round(P,2)) #округлить
di=sqrt(b**2+c**2) #убрать math/добавить * для возведения в степень
print("Ristküliku diagonaal", round(di,2)) #поставить вторую скобку 
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #неправильные ковычки/добаить float
d=2*r #умножить
print("Ringi läbimõõt", d) #поставить запятую / +str(d))
S=pi*r**2 #pi это константа/убрать скобки/добавить *
print("Ringi pindala", round(S))
C=2*pi*r #умножение/убрать скобки
print("Ringjoone pikkus", round(C)) #поставить вторую скобку
