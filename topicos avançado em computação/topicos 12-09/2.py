altura = int(input("digite a altura: "))
base = int(input("digite a base: "))
def retangulo (b, h):
    area = b*h
    perimetro = b*2 + h*2
    return area, perimetro
area, perimetro = retangulo
print(area, perimetro)