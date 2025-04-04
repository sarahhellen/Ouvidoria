from ouvidoria import *

conn = criarConexao('127.0.0.1','root','12345','ouvidoria')

codigoFilme = int(input("Digite o código: "))
consultaPesquisaFilmes = 'select * from filme where codigo = %s'
dados = [ codigoFilme ]

filmes = listarBancoDados(conn,consultaPesquisaFilmes,dados)

if len(filmes) == 0:
    print("Não existem filmes a serem exibidos")
else:
    print("Filme encontrado: Nome do Filme:", filmes[0][1], "no ano", filmes[0][3])


encerrarConexao(conn)