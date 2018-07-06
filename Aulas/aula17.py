# Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar uma posição do vetor (lista).

# lista = [""]* 101
# p = 0
#
# while p < len(lista):
#     lista[p] = p
#     p+=1

# Mostre na tela todos os números do vetor em ordem crescente (1 a 100)

# lista = [""]* 100
# p = 0
#
# while p < len(lista):
#     lista[p] = p + 1
#     print(lista[p])
#     p+=1

# Mostre na tela todos os números do vetor em ordem decrescente (100 a 1)

# lista = [""]*100
# p = len(lista)
# while p >= 1 :
#     p-=1
#     print(p)
#
# print("De traz para frente.")

# Mostre na tela o dobro de todos os números.

# lista = [""]* 100
# p = 0
# dobro = 0
#
# while p < len(lista):
#     lista[p] = p + 1
#     dobro = lista[p] * 2
#     print(dobro)
#     p+=1

# Apresente na tela a soma de todos os números.

# lista = [""]* 100
# p = 0
# while p < len(lista):
#     lista[p] = p + 1
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

# Apresente na tela a média geral dos valores contidos na lista.

# lista = [""]* 100
# p = 0
# while p < len(lista):
#     lista[p] = p + 1
#     p+=1
#
# p = 0
# soma = 0
#
# while p < len(lista):
#     soma = soma + lista[p]
#     p+=1
#
# print("A média é", soma/len(lista))

# Mostre na tela a quantidade de números pares.

# lista = [""]* 100
# p = 0
# while p < len(lista):
#     lista[p] = p + 1
#     p+=1
#
# par = 0
# p = 0
# while p < len(lista):
#     if lista[p]%2 ==0:
#         par = par + 1
#
#     p+=1
#
# print("A quantidade de pares é: ", par)

# Faça um programa para armazenar 6 números inteiros para uma loteria,
# permitindo que o usuário informe os números sorteados.
# Depois de preencher, informe uma mensagem e os números sorteados.

# lista = [""] * 5
# p = 0
#
# while p < len(lista):
#     lista[p] = int(input("Informe os números sorteados: "))
#     p+=1
#
# print("Os números sorteados foram: ")
#
# p = 0
# while p < len(lista):
#     print("Número: ",lista[p])
#     p+=1

# Um professor precisa armazenar em uma lista os nomes dos alunos presentes
# em um minicurso. Faça um programa para armazenar 5 nomes e permitir que o
# professor digite o nome da cada um. Em seguida, apresente na tela todos
# os nomes informados.

# Faça um programa que peça para o usuário informar o tamanho de um vetor.
# Em seguida, crie este vetor e preencha ele com números digitados pelo usuário.
# Por fim, apresente na tela os números digitados.

# t = int(input("Lista: "))
#
# lista = [""]* t
# p = 0
# while p < len(lista):
#     lista[p] = int(input("Número: "))
#     p+=1
#
# print("Os números digitados foram: ")
#
# p = 0
# while p < len(lista):
#     print("Número: ",lista[p])
#     p+=1

# Para os exercícios abaixo, utilize o vetor criado no exercício anterior.
# Apresente os números do vetor em ordem inversa.

# t = int(input("Lista: "))
# lista = [""]*t
#
# p = 0
# while p < len(lista):
#     lista[p] = int(input("Número: "))
#     p+=1
#
# p = len(lista) - 1
# while p >= 0:
#     print("Posição",p,"- Valor: ",lista[p])
#     p = p - 1

# Apresente a soma de todos os elementos.

# t = int(input("Lista: "))
# lista = [""]*t
#
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

# Calcule a média aritmética dos valores.

# t = int(input("Lista: "))
# lista = [""]*t
#
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
# print("A média é", soma/len(lista))

# Determinar um segmento informado pelo usuário (posição inicial e final)
# para apresentar os números na tela. Por exemplo: na sequência 5, 2, -2,
# -7, 3, 14, 10, -3, 9, -6, 4, 1 o usuário teria que informar 4 e 8 (posição
# inicial e final, respectivamente) para mostrar na tela somente os valores
# destacados.
 
