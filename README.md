<body>
    <center>
  <h1 align="center"> Ouvidoria da Universidade XYZ </h1>
  <br>
      <div align="center">
        </div>

<div align="center">
  <table>
    <tr>
      <td>
        <ul>
          <li><b>A Ouvidoria da Universidade XYZ é o espaço certo pra você dar a sua opinião sobre o que acontece na universidade. Aqui, você pode enviar sugestões, fazer reclamações, deixar críticas construtivas ou até elogiar quando algo der certo (adoramos elogios!). A ideia é ouvir você de verdade e usar esse feedback pra melhorar cada vez mais o nosso ambiente acadêmico. Fique à vontade para se expressar — a casa é sua também!</li>
        </ul>
      </td>
      <td>
        <img src="[https://github.com/user-attachments/assets/716b2e48-29f0-42a3-bf88-37b83edffc66](https://github.com/user-attachments/assets/b316ab88-0a27-4569-941f-b3ce8613c71a)" width="150px" style="border-radius: 10px;">

   ![ChatGPT Image 6 de abr  de 2025, 10_35_00](https://github.com/user-attachments/assets/b316ab88-0a27-4569-941f-b3ce8613c71a)
      </td>
    </tr>
  </table>
</div>


<br>
<br>
<br>
<br>


<h1 align="center"> Apresentação do Código da Ouvidoria Universitária:  </h1>

<br>

# 1. Conexão com Banco de Dados
```python
conx = criarConexao("localhost","root","12345","ouvidoriaxyz")
```
- Estabelece conexão com o banco de dados MySQL.
- **Parâmetros:** servidor, usuário, senha e nome do banco.

 <br>

# 2. Menu Principal
```python
while opcao != 7:
    print("\nMenu de opções: \n1) Listagem...")  # Menu completo
    opcao = int(input("Digite a opção: "))
```
- Loop principal que mantém o sistema em execução.
- Oferece 7 opções de interação.

<br>

# 3. Operações Disponíveis

<br>

## 🔍 Listagem de Manifestações
```python
consultaListagem = "select * from manifestacoes"
descricao = listarBancoDados(conx, consultaListagem)
```
- Exibe todas as manifestações cadastradas
- Mostra código, descrição, tipo, autor e ouvidor


## 🏷️ Listagem por Tipo
```python
consultaListagemTipo = "select * from manifestacoes where tipo like %s"
```
- Filtra manifestações por tipo (Reclamação/Elogio/Sugestão)
- Interface amigável para seleção do tipo


## ➕ Cadastro de Nova Manifestação
```python
consultaInsert = "insert into manifestacoes values (%s,%s,%s,%s)"
insertNoBancoDados(conx,consultaInsert,dados)
```
- **Coleta:** descrição, autor, ouvidor e tipo
- Valida campos obrigatórios
- Retorna código da nova manifestação


## 🔢 Contagem de Manifestações
```python
consultaListagem = "select count(*) from manifestacoes"
```
- Exibe quantidade total de registros


## 📄 Pesquisa por Código
```python
consultaPesquisa = "select * from manifestacoes where codigo = %s"
```
- Localiza manifestação específica
- Exibe todos os detalhes do registro


## ❌ Remoção de Manifestação
```python
consultaRemover = "delete from manifestacoes where codigo = %s"
```
- Remove registro permanentemente
- Verifica existência do código antes de deletar

<br>

# ⚙️ Estrutura do Banco de Dados
## A tabela manifestacoes deve conter:
- Código (chave primária)
- Manifestacao (texto da manifestação)
- Autor (nome do solicitante)
- Ouvidor (responsável pelo registro)
- Tipo (Reclamação/Elogio/Sugestão)

<br>

# 🚀 Como Executar:
1) Configure o banco de dados MySQL
2) Instale as dependências necessárias
3) Execute o arquivo Python principal
4) Interaja com o sistema através do menu

<br>

# ⁉️Observação
- Requer o módulo **operacoesbd.py** para operações de banco de dados!

https://github.com/daniel-abella/operacoesbd/tree/main

- Utilize clicando no link acima e siga os passos!
1) Entre no link eclique em "operacoesbd.py".
2) Vá no canto superior direito e clique na setinha de fazer dowload.
3) Cheque se o dowload foi feito no canto superior direito.
4) Ao clicar na pequena pastinha no arquivo baixado, você será redirecionado onde esse aqruivo ficou em sua máquina.
5) Dando um click encima do aqruivo seguido do comando "ctrl+c", você deverá, em seguida, abrir o Pycharm.
6) Abrindo o Pycharm em seu projeto, aperte o comando "ctrl+v" na área limpa da esquerda (onde ficam os files).
7) Clique em "OK" e você já poderá ver esse file dentro de seu projeto, prontinho para usar!
 
![ezgif com-animated-gif-maker (2)](https://github.com/user-attachments/assets/fd6690fc-c07d-4627-a9f9-263eb10a855e)


</div>
