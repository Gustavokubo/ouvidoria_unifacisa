from operacoesbd import *
import os

def menu():
    print('====================================')
    print('# Bem vindo à ouvidoria Unifacisa # ')
    print('====================================')
    print('1) Listar reclamações.              ')
    print('2) Adicionar reclamação.            ')
    print('3) Remover reclamação.              ')
    print('4) Pesquisar reclamação pelo código.')
    print('5) Sair do sistema de ouvidoria.    ')
    print('====================================')
    print()

    opcao = input('Digite sua opção: ')

    return opcao

def listarReclamacoes(conexao):
    os.system('cls')
    consultaListagem = 'select * from reclamacoes'
    listaReclamacoes = listarBancoDados(conexao, consultaListagem)

    if len(listaReclamacoes) == 0:
        print('Não existem reclamações cadastradas até o momento.')
        print()
        input('Aperte "ENTER" para voltar as opções')
        os.system('cls')

    else:
        print('============================')
        print('     Listar reclamações     ')
        print('============================')

        for manifestacao in listaReclamacoes:
            print('Código', manifestacao[0], '- Reclamação:', manifestacao[1])

        print()
        input('Aperte "ENTER" para voltar as opções')
        os.system('cls')

def inserirNovaReclamacao(conexao):
    os.system('cls')
    novaReclamacao = input('Por favor, digite sua reclamação, em seguida, aperte "ENTER" ')
    print()

    if novaReclamacao == ' ' or len(novaReclamacao) < 5 or novaReclamacao == ' ' * len(novaReclamacao) \
    or novaReclamacao == novaReclamacao[0] * len(novaReclamacao):
        print('Descrição inválida. Por favor, digite algum texto sobre a sua reclamação.')
        print()
        print('Aperte "ENTER" para voltar as opções')
        os.system('cls')

    else:
        consultarNovaReclamacao = 'insert into reclamacoes (reclamacao) values (%s)'
        dados = (novaReclamacao,)
        insertNoBancoDados(conexao, consultarNovaReclamacao, dados)

        consultaCodigo = 'select MAX(codigo) from reclamacoes'
        codigoAdicionado = listarBancoDados(conexao, consultaCodigo)

        for reclamacao in codigoAdicionado:
            print(f'A reclamação foi adicionada com sucesso! O código da reclamação é {reclamacao[0]}.')
            print()
            print('Aperte "ENTER" para voltar as opções')
            os.system('cls')

def removerReclamacoes(conexao):
    os.system('cls')
    consultaListagem = 'select * from reclamacoes'
    listaReclamacoes = listarBancoDados(conexao, consultaListagem)

    if len(listaReclamacoes) == 0:
        print('Não existem reclamações cadastradas até o momento.')
        print()
        input('Aperte "ENTER" para voltar as opções')
        os.system('cls')

    else:
        print('============================')
        print('     Listar reclamações     ')
        print('============================')

        for manifestacao in listaReclamacoes:
            print('Código', manifestacao[0], '- Reclamação:', manifestacao[1])

        print()
        codigoRemover = input('Por favor, digite o código da reclamação que deseja remover: ')

        try:
            codigoRemoverInt = int(codigoRemover)

        except:
            print()
            print('Código inválido. Por favor, digite apenas números de acordo com a listagem.')
            input('Aperte "ENTER" para voltar as opções')
            os.system('cls')

        else:
            consultarRemoverReclamacao = 'delete from reclamacoes where codigo = %s'
            dados = (codigoRemoverInt,)

            reclamacaoRemovidas = excluirBancoDados(conexao, consultarRemoverReclamacao, dados)

            if reclamacaoRemovidas == 0:
                print()
                print('Código inválido. Por favor, digite apenas números de acordo com a listagem')
                print()
                input('Aperte "ENTER" para voltar as opções')
                os.system('cls')

            else:
                print()
                print('Reclamação removida com sucesso!')
                input('Aperte "ENTER" para voltar as opções')
                os.system('cls')

def pesquisarReclamacoes(conexao):
    os.system('cls')
    consultaListagem = 'select * from reclamacoes'
    listaReclamacoes = listarBancoDados(conexao, consultaListagem)

    if len(listaReclamacoes) == 0:
        print('Não existem reclamações cadastradas até o momento.')
        print()
        input('Aperte "ENTER" para voltar as opções')
        os.system('cls')

    else:
        print('============================')
        print('     Listar reclamações     ')
        print('============================')

        for manifestacao in listaReclamacoes:
            print('Código', manifestacao[0])

        print()
        codigoPesquisa = input('Digite o código referente à reclamação: ')

        try:
            codigoPesquisaInt = int(codigoPesquisa)

        except:
            print()
            print('Código inválido. Por favor, digite apenas números de acordo com a listagem.')
            input('Aperte "ENTER" para voltar as opções')
            os.system('cls')

        else:
            consultaListagem = 'select * from reclamacoes where codigo = ' + codigoPesquisa
            listaReclamacoes = listarBancoDados(conexao, consultaListagem)

            if len(listaReclamacoes) == 0:
                print('Não existem reclamações cadastradas com o código informado.')
                print()
                input('Aperte "ENTER" para voltar as opções')
                os.system('cls')

            else:
                print()
                print('Resposta da pesquisa:')
                for manifestacao in listaReclamacoes:
                    print('Código', manifestacao[0], '- Reclamação:', manifestacao[1])
                print()
                input('Aperte "ENTER" para voltar as opções')
                os.system('cls')

def agradecimento():
    os.system('cls')
    print('')
    print('Muito obrigado por utilizar o sistem de ouvidoria da unifacisa!')
    print('')

def opcaoInvalida():
    os.system('cls')
    print('Opção inválida. Por favor, escolha uma opção do menu.')
    print('')
    input('Aperte "ENTER" para voltar as opções')
    os.system('cls')






