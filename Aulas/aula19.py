# import randon
#
# randon.randint(1,60)
#
# from randon import randint
#
# randint(1,60)

                             # gera número com repetição

# from random import randint
#
# loteria = [""] * 6
# i = 0
#
# while i < len(loteria):
#     loteria[i] = randint(1,60)
#     i += 1
#
# print(loteria)

                              # randon sem repetir número

# from random import randint
#
# loteria = [""] * 6
# i = 0
#
# while i < len(loteria):
#     num = randint(1,60)
#
#     repetiu = "n"
#
#     k = 0
#     while k < i:
#
#         if num == loteria[k]:
#             i -= 1
#
#             repetiu = "s"
#
#             break
#
#         k += 1
#
#     if repetiu == "n":
#
#         loteria[i] = num
#
#     i += 1
#
# print(loteria)
                              # Versão Python facil
# numeros = []
#
# while len(numeros) < 6:
#
#     num = randint(1,60)
#
#     if num not in numeros:
#
#         numeros.append(num)
#
# print(numeros)
