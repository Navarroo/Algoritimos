import sqlite3

def contatos(conexao):
    cursor = conexao.cursor()
    sql = '''
       CREATE TABLE IF NOT EXISTS contato(
        nome text,
        fone text,
        email text,
        usuario integer
       );

    '''

    cursor.execute(sql)

def inserir_contato(conexao,nome,fone,email,usuario):
    cursor = conexao.cursor()

    sql = '''

        INSERT INTO contato VALUES (
            '{}',
            '{}',
            '{}',
            {}
        );
    '''.format(nome, fone, email, usuario)

    cursor.execute(sql)
    conexao.commit()

def Consultar_conts(conexao):
    cursor = conexao.cursor()
    sql = '''    SELECT rowid, * FROM contato ;'''

    cursor.execute(sql)
    print("Listando todos os dados inseridos na tabela... \n \n ")
    for usr in cursor.fetchall():
        print( "{} - {} ({})".format(usr[0], usr[1], usr[2]) )

def buscar_conts(conexao):
    cursor = conexao.cursor()
    condicao = input("\n \n Isira o nome que deseja consutar: ")
    sql = '''
        SELECT rowid, * FROM contato
         WHERE nome LIKE '%{}%' ;
    '''.format(condicao)
    cursor.execute(sql)
    for linha in cursor.fetchall():
        print(linha)

def deletar_conts(conexao):
    cursor = conexao.cursor()
    condicao = int (input ("Digite o ID do usuário que deseja apagar os dados: "))

    sql = ''' DELETE FROM contato
              WHERE rowid LIKE '%{}%';

    '''.format(condicao)
    cursor.execute(sql)
    conexao.commit()

    print("Mostrando a tabela atual...")
    for usr in cursor.fetchall():
        print( "{} - {} ({})".format(usr[0], usr[1], usr[2]) )

def update_conts(conexao):
    cursor = conexao.cursor()
    print("""
    \t\t Escolha a opção que deseja atualizar \n\n
    \n\t\t 1- Nome
    \n\t\t 2- fone
    \n\t\t 3- email
    """)
    esc = int(input("Opção: "))
    if esc == 1:
        idusu = input("Informe o ID do usuário: ")
        altnome = input("Novo nome: ")
        sql = ''' UPDATE contato
                  SET nome = '{}'
                  WHERE rowid = '{}'

            '''.format(altnome,idusu)

    elif esc == 2:
        idusu = input("Informe o ID do usuário: ")
        altlogin = input("Novo login: ")
        sql = ''' UPDATE contato
                  SET fone = '{}'
                  WHERE rowid = '{}'

            '''.format(altlogin,idusu)

    elif esc == 3:
        idusu = input("Informe o ID do usuário: ")
        altsenha = input("Nova senha: ")
        sql = ''' UPDATE contato
                  SET email = '{}'
                  WHERE rowid = '{}'

            '''.format(altsenha,idusu)
    cursor.execute(sql)
    conexao.commit()



print("Conectando no banco... \n")
conexao = sqlite3.connect("BANCO.sqlite")
contatos(conexao)

def opcao_conts():
    progma_on = True
    while progma_on == True:
        print('''\n \n ----- MENU CONTATO ---
        1- Inserir contato.
        2- Listar contato.
        3- Buscar um contato específico.
        4- Deletar contato
        5- Atualizar...
        6- Sair
        \n \n''')
        escolha = int(input("\nEscolha uma das opções: "))
        print("\n \n")
        if escolha == 1:
            nome = input("Nome: ")
            fone = input("Fone: ")
            email = input("Email: ")
            usuario = int(input("Usuário: "))
            inserir_contato(conexao,nome,fone,email,usuario)

        elif escolha == 2:
            Consultar_conts(conexao)
        elif escolha == 3:
            buscar_conts(conexao)
        elif escolha == 4:
            deletar_conts(conexao)
        elif escolha == 5:
            update_conts(conexao)
        else:
            progma_on = False


    print("\n \n")
    print("Fechando o banco... \n")
    conexao.close()
