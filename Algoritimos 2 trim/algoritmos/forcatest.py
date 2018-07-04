# https://killdragonsblog.wordpress.com/2016/05/18/projetando1-joguinho-de-forca-dinamico-em-python-como-foi-o-processo/

palavras_jogo = ["abacaxi",
                 "elefante",
                 "tomate",
                 "caneca"
                 ]

dicas = ["É uma fruta",
         "Um animal de grande porte",
         "Uma fruta",
         "Recipiente de bebidas"
         ]
frase = [" "]
letras = [" "]

letras_digitadas = []

import random

palavras_jogo = random.choice(palavras_jogo)
print(palavras_jogo)

frase = ["_"] * len(palavras_jogo)

for letras_digitadas in frase:
    palavras_jogo += letras_digitadas.upper()

for letras_digitadas in palavras_jogo:
    if letras_digitadas == " ":
        letras += [" "]

    else:
        letras += ["_"]



p = 2
while p != 3:

    print("BEM VINDO AO JOGO DA FORCA \n ")
    print("Você terá 6 chances  \n")
    jogando = input("Você está pronto(a) para jogar? \n" "sim \n" "não \n")



    if jogando == "sim":
        print("Let's que let's \n")

        print("-------------  ")
        print("|           |  ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|")

        erros = 0
        while erros < 6:
            letras = str(input("Escolha uma letra: "))
            letras_digitadas.append(letras)
            print("-------------  ")
            print("|           |  ")
            print("|              ")
            print("|              ")
            print("|              ")
            print("|              ")
            print("|              ")
            print("|")

            if letras not in palavras_jogo:
                erros += 1

                if erros == 1:
                    print("-------------  ")
                    print("|           |  ")
                    print("|         (º-º)")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|")

                elif erros == 2:
                    print("-------------  ")
                    print("|           |  ")
                    print("|         (º-º)")
                    print("|           |  ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|")

                elif erros == 3:
                    print("-------------  ")
                    print("|           |  ")
                    print("|         (º-º)")
                    print("|          /|  ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|")

                elif erros == 4:
                    print("-------------  ")
                    print("|           |  ")
                    print("|         (º-º)")
                    print("|          /|\ ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|")

                elif erros == 5:
                    print("-------------  ")
                    print("|           |  ")
                    print("|         (º-º)")
                    print("|          /|\ ")
                    print("|          /   ")
                    print("|              ")
                    print("|              ")
                    print("|")

                elif erros == 6:
                    print("Você Perdeu... (õ_õ)")
                    print("-------------       ")
                    print("|           |       ")
                    print("|         (x_x)     ")
                    print("|          /|\      ")
                    print("|          / \\     ")
                    print("|                   ")
                    print("|                   ")
                    print("|")

    elif jogando == "não":
        print("Esperava mais de você... ")
        p += 1

    else:
        print("Escolha sim ou não, meu chapa \n")



print(letras_digitadas)
