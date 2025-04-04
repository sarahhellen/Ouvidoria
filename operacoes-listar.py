from operacoesbd import *

conn = criarConexao('127.0.0.1','root','12345','locadora_ana')

consultaListagemFilmes = 'select * from filme'
filmes = listarBancoDados(conn,consultaListagemFilmes)

if len(filmes) == 0:
    print("Não existem filmes a serem exibidos")
else:
    print("Lista de Itens")
    for item in filmes:
        print("- Nome do Filme:", item[1], "no ano", item[3])

encerrarConexao(conn)