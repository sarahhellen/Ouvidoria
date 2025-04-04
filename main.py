from operacoesbd import *
opcao = 1

conn = criarConexao('127.0.0.1','root','12345','ouvidoria')

while opcao != 6:
    print("\n1) Listar \n2) Adicionar \n3) Pesquisar \n4) Remover \n5) Substituir \n6) Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        consultaListagemFilmes = 'select * from filme'
        filmes = listarBancoDados(conn, consultaListagemFilmes)

        if len(filmes) == 0:
            print("Não existem filmes a serem exibidos")
        else:
            print("Lista de Itens")
            for item in filmes:
                print("- Nome do Filme:", item[1], "no ano", item[3])

    elif opcao == 2:
        nomeFilme = input("Digite o nome do novo filme: ")
        sinopseFilme = input("Digite a sinopse do novo filme: ")
        anoFilme = int(input("Digite o ano do novo filme: "))

        consultaInsert = 'insert into Filme (nome,sinopse,ano) values (%s,%s,%s)'
        dados = [nomeFilme, sinopseFilme, anoFilme]

        insertNoBancoDados(conn, consultaInsert, dados)
        print("Filme cadastrado com sucesso!")

    elif opcao == 3:
        codigoFilme = int(input("Digite o código: "))
        consultaPesquisaFilmes = 'select * from filme where codigo = %s'
        dados = [codigoFilme]

        filmes = listarBancoDados(conn, consultaPesquisaFilmes, dados)

        if len(filmes) == 0:
            print("Não existem filmes a serem exibidos")
        else:
            print("Filme encontrado: Nome do Filme:", filmes[0][1], "no ano", filmes[0][3])


    elif opcao != 6:
        print("Opção Inválida!")

encerrarConexao(conn)
print("Obrigado por usar o sistema de ouvidoria!")