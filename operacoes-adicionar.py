from ouvidoria import *

conn = criarConexao('127.0.0.1','root','12345','ouvidoria')

nomeFilme = input("Digite o nome do novo filme: ")
sinopseFilme = input("Digite a sinopse do novo filme: ")
anoFilme = int(input("Digite o ano do novo filme: "))

consultaInsert = 'insert into Filme (nome,sinopse,ano) values (%s,%s,%s)'
dados = [ nomeFilme, sinopseFilme, anoFilme ]

insertNoBancoDados(conn,consultaInsert,dados)
print("Filme cadastrado com sucesso!")

encerrarConexao(conn)