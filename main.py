from ouvidoriabd import *
opcao = 1

conn = criarConexao('127.0.0.1','root','Yennefer8!','ouvidoria')

while opcao != 7:
    print("\n1) Listar manifestações \n2) Listagem de manifestações por tipo \n3) Criar manifestação \n4) Exibir quantidade de manifestações \n5) Pesquisar manifestação por código \n6) Excluir manifestação por código \n7) Sair do sistema")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        consultaListagem = "select * from manifestacao"
        manifestacao = listarBancoDados(conn, consultaListagem)

        if len(manifestacao) == 0:
            print("Nenhuma manifestação cadastrada.")
        else:
            print("Lista de Manifestações: ")
            for item in manifestacao:
                print("Manifestação de Código", str(item[0]) + ":", item[1], "\n Tipo:", item[4], "\n Autor:", item[2], "\n Ouvidor:", item[3])


    elif opcao == 2:
        while True:
            tipolistagem = int(input(" Qual tipo de manifestação a listar \n 1) Reclamação \n 2) Elogio \n 3) Sugestão \n Digite o código da manifestação desejada: "))
            if tipolistagem == 1:
                tipo = "Reclamação"
                break
            elif tipolistagem == 2:
                tipo = "Elogio"
                break
            elif tipolistagem == 3:
                tipo = "Sugestão"
                break
            else:
                print("Opção inválida. Tente novamente.\n")

        consultaListagemTipo = "select * from manifestacao where tipo like %s"
        dados = [tipo]
        manifestacao = listarBancoDados(conn, consultaListagemTipo, dados)
        if len(manifestacao) == 0:
            print("Nenhuma manifestação cadastrada.")
        else:
            print("Lista de Manifestações do tipo", tipo.capitalize())
            for item in manifestacao:
                print("Manifestação de Código", str(item[0]) + ":", item[1], "\n Tipo:", item[4], "\n Autor:", item[2],"\n Ouvidor:", item[3])

    elif opcao == 3:
        novaManifestacao = input("Nova manifestação: ")
        autor = input("Digite seu nome completo: ")
        ouvidor = input("Nome do Ouvidor: ")
        while True:
            tipoNovaManifestacao = int(input(
                "Tipos de Manifestações: \n 1) Reclamação \n 2) Elogio \n 3) Sugestão \nTipo da Nova Manifestação: "))

            if tipoNovaManifestacao == 1:
                tipo = "Reclamação"
                break
            elif tipoNovaManifestacao == 2:
                tipo = "Elogio"
                break
            elif tipoNovaManifestacao == 3:
                tipo = "Sugestão"
                break
            else:
                print("Opção inválida. Tente novamente.\n")

        consultaInsert = "insert into manifestacao (descricao,autor,ouvidor,tipo) values (%s,%s,%s,%s)"
        dados = [novaManifestacao, autor, ouvidor, tipo]

        if novaManifestacao == "" or autor == "" or ouvidor == "":
            print("Manifestação ou Tipo inválido.")

        else:
            insertNoBancoDados(conn, consultaInsert, dados)
            consultaCodigo = "select codigo from manifestacao where descricao like %s"
            dados = [novaManifestacao]
            manifestacao = listarBancoDados(conn, consultaCodigo, dados)
            cod = manifestacao[0]
            print("Manifestação cadastrada com sucesso. Seu código é: ", cod[0])

    elif opcao == 4:
        consultaListagem = "select count(*) from manifestacao"
        resultado = listarBancoDados(conn, consultaListagem)
        quantidadeManifestacoes = resultado[0][0]
        if resultado == 0:
            print("Nenhuma manifestação cadastrada.")
        else:
            print("Até o momento, o sistema possui exatas", quantidadeManifestacoes, "manifestações.")

    elif opcao == 5:
        codigoManifestacao = int(input("Por favor, informe o código da manifestação: "))
        consultaPesquisa = "select * from manifestacao where codigo = %s"
        dados = [codigoManifestacao]

        manifestacao = listarBancoDados(conn, consultaPesquisa, dados)

        if len(manifestacao) == 0:
            print("Nenhuma manifestação a ser exibida ou código inválido.")

        else:
            print("A manifestação de código", codigoManifestacao, "é:", manifestacao[0][1], "\nTipo:", manifestacao[0][4])

    elif opcao == 6:
        codigoManifestacao = int(input("Por favor, informe o código da manifestação a remover: "))

        consultaRemover = "delete from manifestacao where codigo = %s"
        dados = [codigoManifestacao]

        linhasAlteradas = excluirBancoDados(conn, consultaRemover, dados)

        if linhasAlteradas == 0:
            print("Erro ao remover, código inválido.")

        else:
            print("Manifestação removida com sucesso!")

    elif opcao != 7:
        print("Opção inválida. Tente novamente! ")

print("A Universidade XYZ agradece a colaboração!")

encerrarConexao(conn)