from ouvidoriabd import *

conn = criarConexao('localhost','root','Yennefer8!','ouvidoria')

novaManifestacao = input("Nova manifestação: ")
autor = input("Digite seu nome completo: ")
ouvidor = input("Nome do Ouvidor: ")
while True:
    tipoNovaManifestacao = int(input("Tipos de Manifestações: \n 1) Reclamação \n 2) Elogio \n 3) Sugestão \nTipo da Nova Manifestação: "))

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

encerrarConexao(conn)
