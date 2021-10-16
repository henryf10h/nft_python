# GENERATE RANDOM NUMBER, READ IT AND DIVIDE IT BETWEEN ALL.

# GENES :
# borde[5], ojos[5], bocas[5], cyb[8], inferior[4], six[6], cuerpo[1].       




def foo(num):
    genes = []
    for i in range(9):
        a = str(num)[:2]
        b = str(num)[2:] 
        num = int(b)
        genes.append(int(a))
    return genes

if __name__ == '__main__':
    foo()

