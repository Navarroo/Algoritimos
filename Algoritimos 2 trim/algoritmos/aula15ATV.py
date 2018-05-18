# ====== S O M A = E = M É D I A======

# t = int(input("Lista: "))
#
# lista = [""]* t
# p = 0
# while p < len(lista):
#     lista[p] = int(input("Número: "))
#     p+=1
#
# p = 0
# soma = 0
#
# while p < len(lista):
#     soma = soma + lista[p]
#     p+=1
#
# print("A soma é",soma)
# print("A média é", soma/len(lista))

# ====== M É D I A = P O N D E R A D A =====

t = int(input("Lista: "))

lista = [""]* t
p = 0
while p < len(lista):
    lista[p] = int(input("Número: "))
    p+=1


soma = 0
pesos = 0
p = 0
while p < len(lista):
    soma = soma + (lista[p]*p)
    pesos = pesos + p
    p+=1

medpon = soma / pesos
print ("Média ponderada: ", medpon)
