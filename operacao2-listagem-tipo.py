from ouvidoriabd import *

conn = criarConexao('localhost','root','Yennefer8!','ouvidoria')

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

encerrarConexao(conn)