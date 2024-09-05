arqd = open( "c://temp//7n0i_1.pdb", "r" )

dic = {}
for i in arqd:
    atomo = i[77:78]
    if atomo in dic:
        dic[atomo] += 1
    else:
        dic[atomo] = 1

for atomo in dic:
    print( atomo, " = ", dic[atomo] ) 

arqd.close()
