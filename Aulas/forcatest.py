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

letras_digitadas = []
letras_acertos= []
letras_erros=[]

import random

palavras_jogo = random.choice(palavras_jogo)
print(palavras_jogo)

p = 2
while p != 3:

    print("BEM VINDO AO JOGO DA FORCA \n ")
    print("Você terá 6 chances  \n")
    jogando = str(input("Você está pronto(a) para jogar? \n" "sim \n" "não \n R: "))

    if jogando == "sim":
        print("Let's que let's \n")

        erros = 0
        while erros != 6:

            letras = str(input("Escolha uma letra: \n"))
            letras_digitadas.append(letras)

            if letras in palavras_jogo:
                letras_acertos += letras_digitadas
                print("Letras digitadas",letras_digitadas)

            elif letras not in palavras_jogo:
                letras_erros += letras_digitadas
                print("Letras digitadas",letras_digitadas, "\n")
                erros += 1

                if erros ==0:
                    print("-------------  ")
                    print("|           |  ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|")

                elif erros == 1:
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
                    print("|           Y  ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|")

                elif erros == 3:
                    print("-------------  ")
                    print("|           |  ")
                    print("|         (º-º)")
                    print("|          /Y  ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|")

                elif erros == 4:
                    print("-------------  ")
                    print("|           |  ")
                    print("|         (º-º)")
                    print("|          /Y\ ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|")

                elif erros == 5:
                    print("-------------  ")
                    print("|           |  ")
                    print("|         (º-º)")
                    print("|          /Y\ ")
                    print("|          /   ")
                    print("|              ")
                    print("|              ")
                    print("|")

                elif erros == 6:
                    print("======VOCÊ É FRACO...(õ_õ)======")
                    print("-------------       ")
                    print("|           |       ")
                    print("|         (x_x)     ")
                    print("|          /Y\      ")
                    print("|          / \\     ")
                    print("|                   ")
                    print("|                   ")
                    print("| \n")
                    p += 1
                    print("Letras digitadas",letras_digitadas, "\n")
    elif jogando == "não":
        print("======ESPERAVA MAIS DE VOCÊ...====== \n")
        p += 1

    else:
        print("ESCOLHA SIM OU NÃO, MEU CHAPA \n")
