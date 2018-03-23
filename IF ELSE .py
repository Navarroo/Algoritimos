# print ("Exercicio 1")
#
# a = input ("Digite um valor: ")
# a = int(a)
#
# if a > 0:
#     print("Esse número é positivo", a)
#
# elif a == 0:
#     print("Esse número é nulo")
#
# else:
#     print("Esse número é negativo", a)
#  # ---------------------------------------------------------
#  print ("Exercicio 2")
#
# num1 = input("Digite um número: ")
# num1 = int(num1)
#
# num2 = input("Digite outro número: ")
# num2 = int(num2)
#
# if num1 > num2:
#     print("O primeiro número é maior.")
#
# elif num2 > num1:
#     print("O segundo é maior.")
# else:
#     print("Os números são iguais.")
#----------------------------------------------------------
# print ("Exercicio 3")
#
# a = int(input("Digite um número: "))
# b = int(input("Digite um número: "))
# c = int(input("Digite um número: "))
#
# d = a + b
#
# if d < c:
#     print(d)
# else:
#     print("")

#----------------------------------------------------------
# print("Exercicio 4")
#
# sexo = input("Digite m para Masculino e f para feminino: ")
#
# if sexo == "m":
#     print("M - Masculino")
# elif sexo == "f":
#     print("F - Feminino")
# else:
#     print("Digite apenas m ou f...")
# #----------------------------------------------------------
# print("Exercicio 5")
#
# n = int(input("Digite um número: "))
#
# a = n % 2
#
# if a == 0:
#     print("O número", n, "é par")
# else:
#     print("O número", n, "é impar")
#-------------------------------------------------------------
# print("Exercicio 6")
#
# n = int(input("Digite um número: "))
#
# a = n % 2
#
# if a == 0:
#     print(n + 5)
# else:
#     print(n + 8)
#-------------------------------------------------------------
# print("Exercicio 7")
#
# trab = int(input("Digite a nota do trabalho: "))
# prova = int(input("Digite a nota da prova: "))
# media = ((trab + prova) / 2)
#
# if media >= 60:
#     print("Você foi aprovado")
#
# else:
#     print("Você foi reprovado")
#---------------------------------------------------------------
# print("Exercicio 8")
#
# a = int(input("Digite um número: "))
# b = int(input("Digite um número: "))
# c = int(input("Digite um número: "))
#
# if (a > b and a > c):
#     print(a)
#
# elif (b > a and b > c):
#     print(b)
#
# else:
#     print(c)
#---------------------------------------------------------------
# print("Exercicio 9")
#
# a = int(input("Digite um número: "))
# b = int(input("Digite um número: "))
# c = int(input("Digite um número: "))
#
# if (a > b and b > c):
#      print(a, b, c)
#
# elif (b > a and a > c):
#      print(b, a, c)
#
# elif (a > b and c > b):
#     print(a, c, b)
#
# elif (b > c and c > a):
#     print(b, c, a)
#
# elif (c > a and a > b):
#     print(c, a, b)
#
# elif (c > b and b > a):
#     print (c, b, a)
#
# else:
#     print("")
#----------------------------------------------------------------
print("Exercicio 10")

print("========================")
print("     Menu de opções    ")
print("========================")
print("[1] - Somar 2 números")
print("[2] - Potência de um número")
print("[3] - Raiz de grau N")
print(" ")
res = int(input("Opção: "))

if res == 1:
    a = int(input("Digite um número: "))
    b = int(input("Digite mais um número: "))
    print(a + b)

elif res == 3:
    a = input("Digite o valor de A: ")
    a = float(a)

    b = input("Grau da raiz:")
    b = int(b)

    x = a**(1/b)

    print(x)

    print("O resultado é", x)

    print("A raiz de grau", b, "de", a, "é", x)

elif res == 2:
    a = int(input("Digite um número: "))
    b = int(input("Digite a potência: "))
    c = a**b

    print(c)
    
else:
    print("ERRO: A opção não se encontra defenida ! tente novamente!")
