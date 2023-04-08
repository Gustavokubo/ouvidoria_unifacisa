from ouvidoria_metodos import *

opcao = 'ouvidoria'

conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria_unifacisa')

while opcao != '5':
    opcao = menu()

    if opcao == '1':
        listarReclamacoes(conexao)

    elif opcao == '2':
        inserirNovaReclamacao(conexao)

    elif opcao == '3':
        removerReclamacoes(conexao)

    elif opcao == '4':
        pesquisarReclamacoes(conexao)

    elif opcao == '5':
        agradecimento()

    elif opcao != '5':
        opcaoInvalida()

encerrarBancoDados(conexao)

