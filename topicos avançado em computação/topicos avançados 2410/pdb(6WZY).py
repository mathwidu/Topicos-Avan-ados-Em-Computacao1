arq = open("c://temp//6wzy.pdb", "r")
dic= {}

for i in arq:
     if (i[17:20] == "PHE") and (i[13:15] == "CA"):
        contagemphe = i[17:20]
        if contagemphe in dic:
            dic[contagemphe] += 1
        else:
            dic[contagemphe] = 1
for contagemphe in dic:
    print( contagemphe, " = ", dic[contagemphe] )

arq.close()




arq2 = open("c://temp//4mj5.pdb", "r")
dic2= {}

for j in arq2:
     if (j[17:20] == "PHE") and (j[13:15] == "CA"):
        contagemphe2 = j[17:20]
        if contagemphe2 in dic2:
            dic2[contagemphe2] += 1
        else:
            dic2[contagemphe2] = 1
for contagemphe2 in dic2:
    print( contagemphe2, " = ", dic2[contagemphe2] )
arq2.close()


arq3 = open("c://temp//5wop.pdb", "r")
dic3= {}

for l in arq3:
     if (l[17:20] == "PHE") and (l[13:15] == "CA"):
        contagemphe3 = l[17:20]
        if contagemphe3 in dic3:
            dic3[contagemphe3] += 1
        else:
            dic3[contagemphe3] = 1
for contagemphe3 in dic3:
    print( contagemphe3, " = ", dic3[contagemphe3] )
arq3.close()


maior = dic3[contagemphe3] 
if dic2[contagemphe2] > maior:
    maior = dic2[contagemphe2]
elif dic[contagemphe] > maior:
    maior = dic[contagemphe]
