from ouvidoriabd import *

conn = criarConexao('localhost','root','Yennefer8!','ouvidoria')

codigoManifestacao = int(input("Por favor, informe o código da manifestação a remover: "))

consultaRemover = "delete from manifestacao where codigo = %s"
dados = [codigoManifestacao]

linhasAlteradas = excluirBancoDados(conn, consultaRemover, dados)

if linhasAlteradas == 0:
    print("Erro ao remover, código inválido.")

else:
    print("Manifestação removida com sucesso!")

encerrarConexao(conn)