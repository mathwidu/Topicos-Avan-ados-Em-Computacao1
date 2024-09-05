arqd = open( "c://temp//7n0i_1.pdb", "r" )

dic = {}
for i in arqd:
    li = i.split()
    lin = ""
    linha = ""
    for j in li:
        lin = lin + "";"" + j 
    linha = lin[1:]
    print(linha)
arqd.close()
