#
# print("Funções!")
# def tabuada1():
#     x = float(input("Digite um numero pra fazer a tabuada: \n"))
#     n = 0
#     while n <= 10:
#         resultado = x * n
#         print("{} X {} = {}".format(x,n,resultado))
#         n+=1
# tabuada1()
########################################################
# exemplo de função com parâmetro e sem retorno
#
# def exe2(num):
#     if ( num % 2 == 0):
#         print("sdsdfsdf")
#
#     else:
#         print("12312")
#
# q = 10
# exe2(q)
# b = int(input("asdas: "))
# exe2(b)
#
#########################################################

# def exemplo2(n):
#
#     n = 0
#     while n <= 10:
#         resultado = x * n
#         print("{} X {} = {}".format(x,n,resultado))
#         n+=1
# x = float(input("Digite um numero pra fazer a tabuada: \n"))
# exemplo2(x)
########################################################
# def calc_tabuada(n):
#     for x in range(11):
#         print(n,"*",x,"=",x*n)
#
# a = int(input("Escolha uma tabuada: "))
# calc_tabuada(a)
########################################################
def exem3(a):

    triplo = a * 3

    return triplo


def exem4(num):

        if num % 2 == 0:

            return num**2

        else:
            n = num **3
            return n

k = exem4(int(input("Numero: ")))
print(k)
