# -*- coding: cp1251 -*-
import re
my_file = open("Shinel.txt", "r")
samtext = my_file.read()
my_file.close()
mastext = re.split(r'[^\wа-яА-Я]+', samtext)
buk = {}
slov ={}
print ("1. В тексте " + str(len(mastext)) + " слов")

for i in [x.lower() for x in mastext]:      #Временная версия массива mastext с опущенными словами
    slov[i] = slov.get(i, 0) + 1
print ("2. Шинель встречается " + str(slov["шинель"]) + " раз")

z = samtext[:61]
z1 = [x for x in z]
z1.reverse()
z2 = "".join(z1)

print ("3. Первое предложение задом на перёд: " + z2)

for i in [x.lower() for x in samtext]:      #Временная версия строки samtext с опущенными буквами
    if (i >= "а" and i <= "я") or (i >= "А" and i <= "Я") or (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
        buk[i] = buk.get(i, 0) + 1
a = sorted(buk.items(), lambda x,y: cmp(y[1], x[1]))
print ("4. На первом месте топа буква " + a[0][0])
print ("   На втором месте топа буква " + a[1][0])
print ("   На третьем месте топа буква " + a[2][0])
print ("   На первом месте антитопа буква " + a[len(a)-1][0])
print ("   На втором месте антитопа буква " + a[len(a)-2][0])
print ("   На третьем месте антитопа буква " + a[len(a)-3][0])

b = slov.items()
chslov = None
chchisl = 0
for i in b:
    if i[1] > chchisl and len(i[0]) > 3:
        chchisl = i[1]
        chslov = i[0]
print ("5. Самое частовстречающееся слово, длиннее трёх букв это " + chslov)

