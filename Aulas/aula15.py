#criando uma lista vazia
listaVazia = []

#criando uma lista com 10 posições

lista = [""]*10

#Pedir tamanho da lista
t = int(input("Tamanho da lista"))

lista = [""]*t

lista = [""] * 5

#preenchendo uma lista manualmente

lista[0] = 13
lista[1] = 20
lista[2] = 34
lista[3] = 50
lista[4] = 21

#mostrando valores

print("Na primeira posição", lista[0])
print("Na segunda posição", lista[1])
print("Na terceira posição", lista[2])
print("Na quarta posição", lista[3])
print("Na quinta posição", lista[4])

lista[3] = 29


lista = [""]*5
p = 0
while p <= 4:
    lista[p] = input("Número: ")
    lista[p] = int(lista[p])
    p = p + 1

p = 0
while p < len(lista):
    print("Posição",p," - Valor: ",lista[p])
    p+=1
----------------------------------------------
lista = [""]*5
p = 0
while p <= 4:
    lista[p] = input("Número: ")
    lista[p] = int(lista[p])
    p = p + 1

p = len(lista) - 1
while p >= 0:
    print("Posição",p,"- Valor: ",lista[p])
    p = p - 1
------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++
================================================

t = int(input("Lista"))

lista = [""]*t

while p < len(lista) :
    lista[p] = int(input("Número")
    p+=1


====== S O M A ===================================
