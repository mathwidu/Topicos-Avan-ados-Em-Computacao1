import math
def sg (a, b, c):

    delta = (b*b) - (4*a*c)

    if delta < 0:

        return 'raizes', 'complexas'

    else:
        r1 = (-b + math.sqrt(delta))/(2*a)

        r2 = (-b - math.sqrt(delta))/(2*a)
    
    return (r1, r2)

r, s = sg (1, -5, 4)
print (r, s)

r, s = sg (1, 2, 1)
print (r, s)

r,s = sg (4, 2, 4)
print (r, s)
