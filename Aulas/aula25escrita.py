
# ========MODOS DE LEITURA DE ARQUIVOS=========
# r = read ( leitura)
# a = write (escrita)
# w = delete and create new (escrita em arquivo em branco)


# open retorna um endereço para o arquivo
arq = open("arquivos/nomes.txt", "w")

# escreve alguma coisa no arquivo
arq.write("Navarro\n")

nome = input("Informe seu nome: ")
arq.write(nome)
arq.write("\n")

# salva as notificações e salva os arquivos
arq.close()
