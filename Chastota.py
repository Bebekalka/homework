# -*- coding: cp1251 -*-
import re
my_file = open("Shinel.txt", "r")
samtext = my_file.read()
my_file.close()
mastext = re.split(r'[^\wа-яА-Яa-zA-Z]+', samtext)
buk = {}
obb = 0
for i in [x.lower() for x in samtext]:
    if (i >= "а" and i <= "я") or (i >= "А" and i <= "Я") or (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
        buk[i] = buk.get(i, 0) + 1

for i in range (len(mastext)):
    obb += len(mastext[i])


