from ouvidoriabd import *

conn = criarConexao('localhost','root','Yennefer8!','ouvidoria')
opcao = 1

consultaListagem = "select * from manifestacao"
manifestacao = listarBancoDados(conn, consultaListagem)

if len(manifestacao) == 0:
    print("Nenhuma manifestação cadastrada.")
else:
    print("Lista de Manifestações: ")
    for item in manifestacao:
        print("Manifestação de Código", str(item[0]) + ":", item[1], "\n Tipo:", item[4], "\n Autor:", item[2],"\n Ouvidor:", item[3])

encerrarConexao(conn)