from ouvidoriabd import *

conn = criarConexao('localhost','root','Yennefer8!','ouvidoria')

consultaListagem = "select count(*) from manifestacao"
resultado = listarBancoDados(conn, consultaListagem)
quantidadeManifestacoes = resultado[0][0]
if resultado == 0:
    print("Nenhuma manifestação cadastrada.")
else:
    print("Até o momento, o sistema possui exatas", quantidadeManifestacoes, "manifestações.")

encerrarConexao(conn)