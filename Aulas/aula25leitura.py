
# ========MODOS DE LEITURA DE ARQUIVOS=========
# r = read ( leitura)
# a = write (escrita)
# w = delete and create new (escrita em arquivo em branco)


fileh = open("arquivos/nomes.txt", "r")

conteudo = fileh.readlines()

fileh.close()
