from ouvidoriabd import *

conn = criarConexao('localhost','root','Yennefer8!','ouvidoria')

codigoManifestacao = int(input("Por favor, informe o código da manifestação: "))
consultaPesquisa = "select * from manifestacao where codigo = %s"
dados = [codigoManifestacao]

manifestacao = listarBancoDados(conn, consultaPesquisa, dados)

if len(manifestacao) == 0:
    print("Nenhuma manifestação a ser exibida ou código inválido.")

else:
    print("A manifestação de código", codigoManifestacao, "é:", manifestacao[0][1], "\nTipo:",manifestacao[0][4])

encerrarConexao(conn)