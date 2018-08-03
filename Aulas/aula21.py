# Função com parâmetro
# e sem retorno
# print("Funções!")

# O input() e o int() tem
# parâmetro e tem retorno
# num = input("Número:")
# num = int(num)

# a função float() também
# tem retorno e parâmetro
# a = float( input("Número:") )

# A criação de funções é feita com a palavra "def"
# E, geralmente, é feita no início do programa
# def nome():
#     conteúdo/corpo da função
#     bla bla bla
# Aqui limita o fim da função

# Exemplo de função sem retorno e sem parâmetro
def exemplo1():
    print("Olá mundo!")
    print("Não tenho parâmetro")
    print("Não tenho retorno")

    n = input("Seu nome: ")

    if(n != ""):
        print("Olá {}, bem vindo ao programa X.".format(n) )
    else:
        print("Acesso negado!")


##### Fim das funções ####
exemplo1()
