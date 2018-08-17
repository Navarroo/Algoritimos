p = 2
while p != 3:

    print("\t \t==============Bem vindo============== \n")
    print("\t \t Escolha as seguintes opções: \n")
    print("\t \t 1 - Digitar palavras")
    print("\t \t 2 - Exibir palavras listadas")
    print("\t \t 3 - Sair")
    op = int(input("Opção: "))

    if op == 1:
        arq = open("arquivos/palavras.txt", "a")

        # escreve alguma coisa no arquivo

        nome = input("Informe uma palavra: ")
        arq.write(nome)
        arq.write("\n")

        # salva as notificações e salva os arquivos
        arq.close()

    elif op == 2:

        print("Palavras digitadas: \n")

        fileh = open("arquivos/palavras.txt", "r")

        conteudo = fileh.readlines()

        a = 0
        while a < len(conteudo):
            print(conteudo[a])
            a+=1


        fileh.close()


    elif op == 3:
        p += 1


    else:
        print("Opção não conta na lista...")
