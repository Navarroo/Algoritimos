import sqlite3

def criar_tabela_usuario(conexao):
    cursor = conexao.cursor()
    sql = '''
       CREATE TABLE IF NOT EXISTS usuario(
        nome text,
        login text,
        senha text
       );

    '''

    cursor.execute(sql)

def inserir_usuario(conexao,nome,login,senha):
    cursor = conexao.cursor()

    sql = '''

        INSERT INTO usuario VALUES (
            '{}',
            '{}',
            '{}'
        );
    '''.format(nome, login, senha)

    cursor.execute(sql)
    conexao.commit()

def Consultar(conexao):
    cursor = conexao.cursor()
    sql = '''    SELECT rowid, * FROM usuario ;'''

    cursor.execute(sql)
    print("Listando todos os dados inseridos na tabela... \n \n ")
    for usr in cursor.fetchall():
        print( "{} - {} ({})".format(usr[0], usr[1], usr[2]) )

def buscar(conexao):
    cursor = conexao.cursor()
    condicao = input("\n \n Isira o nome que deseja consutar: ")
    sql = '''
        SELECT rowid, * FROM usuario
         WHERE nome LIKE '{}' ;
    '''.format(condicao)
    cursor.execute(sql)
    for linha in cursor.fetchall():
        print(linha)

def deletar(conexao):
    cursor = conexao.cursor()
    condicao = int (input ("Digite o ID do usuário que deseja apagar os dados: "))

    sql = ''' DELETE FROM usuario
              WHERE rowid LIKE '{}';

    '''.format(condicao)
    cursor.execute(sql)
    conexao.commit()

    print("Mostrando a tabela atual...")
    for usr in cursor.fetchall():
        print( "{} - {} ({})".format(usr[0], usr[1], usr[2]) )

def update(conexao):
    cursor = conexao.cursor()
    print("""
    \t\t Escolha a opção que deseja atualizar \n\n
    \n\t\t 1- Nome
    \n\t\t 2- Login
    \n\t\t 3- Senha
    """)
    esc = int(input("Opção: "))
    if esc == 1:
        idusu = input("Informe o ID do usuário: ")
        altnome = input("Novo nome: ")
        sql = ''' UPDATE usuario
                  SET nome = '{}'
                  WHERE rowid = '{}'

            '''.format(altnome,idusu)

    elif esc == 2:
        idusu = input("Informe o ID do usuário: ")
        altlogin = input("Novo login: ")
        sql = ''' UPDATE usuario
                  SET login = '{}'
                  WHERE rowid = '{}'

            '''.format(altlogin,idusu)

    elif esc == 3:
        idusu = input("Informe o ID do usuário: ")
        altsenha = input("Nova senha: ")
        sql = ''' UPDATE usuario
                  SET senha = '{}'
                  WHERE rowid = '{}'

            '''.format(altsenha,idusu)
    cursor.execute(sql)
    conexao.commit()

print("Conectando no banco... \n")
conexao = sqlite3.connect("aula28.sqlite")
criar_tabela_usuario(conexao)

def opcao():
    progma_on = True
    while progma_on == True:
        print('''\n \n ----- MENU Banco de dados ---
        1- Inserir novo usuário.
        2- Listar o banco.
        3- Buscar um usuário específico.
        4- Deletar usuário
        5- Update...
        6- Sair
        \n \n''')
        escolha = int(input("\nEscolha uma das opções: "))
        print("\n \n")
        if escolha == 1:
            nome = input("Nome: ")
            login = input("Login: ")
            senha = input("Senha: ")
            inserir_usuario(conexao,nome,login,senha)
        elif escolha == 2:
            Consultar(conexao)
        elif escolha == 3:
            buscar(conexao)
        elif escolha == 4:
            deletar(conexao)
        elif escolha == 5:
            update(conexao)
        else:
            progma_on = False


    print("\n \n")
    print("Fechando o banco... \n")
    conexao.close()
