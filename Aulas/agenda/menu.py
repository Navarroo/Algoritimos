from contatos import *
from usuario import *



progma_on = True
while progma_on == True:
    print('''\n \n ----- MENU PRINCIPAL ---
    1- Opções de Usuário.
    2- Opções de contato.
    3-
    4-
    5-
    6- Sair
    \n \n''')
    escolha = int(input("\nEscolha uma das opções: "))
    print("\n \n")
    if escolha == 1:
        opcao_user(conexao)
    elif escolha == 2:
        opcao_conts()
    # elif escolha == 3:
    #     buscar(conexao)
    # elif escolha == 4:
    #     deletar(conexao)
    # elif escolha == 5:
    #     update(conexao)
    else:
        progma_on = False


print("\n \n")
print("Fechando o banco... \n")
conexao.close()
