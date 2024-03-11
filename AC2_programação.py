def calcular_raízes(a,b,c):
  
    discriminante=b**2 - 4*a*c
    if discriminante<0:
        return None #não há raízes reais
    elif discriminante ==0:
        raiz= -b / (2*a)
        return raiz, raiz #raiz unica
    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    return raiz1, raiz2
    #exemplo de uso:
    a=1
    b=-3
    c=2
raízes=calcular_raízes(a,b,c)
if raízes:
    print("as raízes são:",raízes)
else:
    print("náo há raízes reais.")


    def bissexto(ano):
        if ano % 4 ==0 and(ano % 100 != 0 or ano % 400 == 0):
            return True
        else: return False

#exemplo de uso:
ano=2024
if bissexto(ano):
    print(f"o ano {ano} é bissexto.")
else:
    print(f"o ano {ano} não é bissexto")