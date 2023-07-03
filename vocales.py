class Vocales(object):
    def contar_a (self, palabra):
        a = palabra
        cont = 0
        for i in range(0,len(a)):
            if a[i] == 'a' or a[i] == 'A':
                cont +=1
        return cont
    def contar_e (self, palabra):
        e = palabra
        cont = 0
        for i in range(0,len(e)):
            if e[i] == 'e' or e[i] == 'E':
                cont +=1
        return cont
vocal = Vocales()
palabra = input()
print(vocal.contar_a(palabra))
print(vocal.contar_e(palabra))    