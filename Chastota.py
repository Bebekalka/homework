# -*- coding: cp1251 -*-
import re

shinel = open("Shinel.txt", "r")
samtext1 = shinel.read()
shinel.close()

sumashed = open("sumasshed.txt", "r")
samtext2 = sumashed.read()
sumashed.close()

viy = open("Viy.txt", "r")
samtext3 = viy.read()
viy.close()

mastext1 = re.split(r'[^\wа-яА-Я]+', samtext1)
mastext2 = re.split(r'[^\wа-яА-Я]+', samtext2)
mastext3 = re.split(r'[^\wа-яА-Я]+', samtext3)

buk1 = {}
buk2 = {}
buk3 = {}

vsebuk1 = 0
vsebuk2 = 0
vsebuk3 = 0

for i in [x.lower() for x in samtext1]:
    if (i >= "а" and i <= "я") or (i >= "А" and i <= "Я"):
        buk1[i] = buk1.get(i, 0) + 1

for i in [x.lower() for x in samtext2]:
    if (i >= "а" and i <= "я") or (i >= "А" and i <= "Я"):
        buk2[i] = buk2.get(i, 0) + 1

for i in [x.lower() for x in samtext3]:
    if (i >= "а" and i <= "я") or (i >= "А" and i <= "Я"):
        buk3[i] = buk3.get(i, 0) + 1
        
for i in range (len(mastext1)):
    vsebuk1 += len(mastext1[i])

for i in range (len(mastext2)):
    vsebuk2 += len(mastext2[i])

for i in range (len(mastext3)):
    vsebuk3 += len(mastext3[i])
    
c = buk1.keys()
c = sorted(c)

print("       Шинель  Зап. сумасшедшего  Вий")
for i in range (32):
    print("Буква " + c[i] +":  " + str(round(buk1[c[i]]*100/vsebuk1, 2)) +
          "%        " + str(round(buk2[c[i]]*100/vsebuk2, 2)) +
          "%      " + str(round(buk3[c[i]]*100/vsebuk3, 2)) + "%")
