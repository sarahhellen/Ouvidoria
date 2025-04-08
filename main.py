from ouvidoriabd import *
opcao = 1
'''
 menu com 7 opções:  
• 1) Listagem das Manifestações 
• 2) Listagem de Manifestações por Tipo 
• 3) Criar uma nova Manifestação  
• 4) Exibir quantidade de manifestações  
• 5) Pesquisar uma manifestação por código 
• 6) Excluir uma Manifestação pelo Código 
• 7) Sair do Sistema.
'''
conn = criarConexao('127.0.0.1','root','Yennefer8!','ouvidoria')

while opcao != 7:
    print("\n1) Listar manifestações \n2) Listagem de manifestações por tipo \n3) Criar manifestação \n4) Exibir quantidade de manifestações \n5) Pesquisar manifestação por código \n6) Excluir manifestação por código \n7) Sair do sistema")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        consultaListagemManifestacao = 'select count(*) from Ouvidoria'
        manifestacoes = listarBancoDados(conn, consultaListagemManifestacao)

        if len(manifestacoes) == 0:
            print("Não existem manifestações a serem exibidas")
        else:
            print("Lista de Manifestações:")
            for manifestacao in manifestacoes:
                print("- Código", manifestacao[0], "tem a seguinte manifestação:", manifestacao[1])

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

        manifestacoes = listarBancoDados(conn, consultaPesquisaFilmes, dados)

        if len(manifestacoes) == 0:
            print("Não existem filmes a serem exibidos")
        else:
            print("Filme encontrado: Nome do Filme:", manifestacoes[0][1], "no ano", manifestacoes[0][3])

    elif opcao == 4:

encerrarConexao(conn)
print("Obrigado por usar o sistema de ouvidoria!")



