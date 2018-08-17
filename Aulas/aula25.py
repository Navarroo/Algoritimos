# ========MODOS DE LEITURA DE ARQUIVOS=========
# r = read ( leitura)
# a = write (escrita)
# w = delete and create new (escrita em arquivo em branco)


fileh = open("arquivos/nomes.txt", "r")

conteudo = fileh.readlines()

a = 0
while a < len(conteudo):
    print(conteudo[a])
    a+=1


fileh.close()
