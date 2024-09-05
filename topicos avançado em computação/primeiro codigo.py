def contagemRegressiva(n):
    if n == 0:
        print ("fogo")
    else:
        contagemRegressiva(n-1)
        print (n)
contagemRegressiva(10)



