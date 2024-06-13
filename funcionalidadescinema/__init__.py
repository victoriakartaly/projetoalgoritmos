import re
filmes = []
usuarios = {}
compra = []
def exibir_menu_principal():
    print('\n---------------Bem-vindo ao Cine Sertão---------------\n')
    print('1- Cadastrar Usuário')
    print('2- Gerenciamento de filmes')
    print('3- Comprar Ingressos')
    print('4- Ver filmes em cartaz essa semana')
    print('0- Logout')

def exibir_menu_adm():
    print('\n---------------Menu do Administrador---------------\n')
    print('1- Cadastrar filme')
    print('2- Buscar filme')
    print('3- Atualizar dados do filme')
    print('4- Remover filme')
    print('5- Mostrar todos os filmes disponíveis')
    print('6- Mostrar todos os ingressos vendidos')
    print('7- Mostrar todos os ingressos vendidos para um filme específico')
    print('8- Gerar TXT com ingressos vendidos para o filme')
    print('9- Alterar/atualizar dados cadastrais do Administrador')
    print('0- Logout')

def exibir_menu_cliente():
    print('\n---------------Menu do Cliente---------------\n')
    print('1- Comprar ingressos')
    print('2- Ver filmes disponíveis')
    print('3- Ver minhas compras')
    print('4- Alterar/atualizar dados cadastrais')
    print('5- Cancelar compra')
    print('0- Logout')

def cadastrar_usuario(usuarios):
    print('\n---------------Cadastro de Usuário---------------\n')
    nome = input('Digite seu nome completo: ')
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    perfil = int(input('Digite 1 para Administrador do cinema ou 2 para Cliente do cinema: '))

    usuarios[login] = {'nome': nome, 'senha': senha, 'perfil': perfil}
    print('Cadastro realizado com sucesso!!!')

def login_usuario(usuarios):
    print('\n---------------Login do Usuário---------------\n')

    while True:
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')

        if (login in usuarios and usuarios[login]['senha'] == senha):
            perfil = usuarios[login]['perfil']
            nome = usuarios[login]['nome']
            print(f'\nLogin realizado com sucesso, {nome}!')

            return perfil  # Retorna o perfil do usuário (1 para administrador, 2 para cliente)
        else:
            print('\nLogin ou senha incorretos. Tente novamente.\n')

def gerenciar_filmes():
    print('\n---------------Gerenciamento de Filmes---------------\n')
    print('Opções:')
    print('1- Cadastrar novo filme')
    print('2- Buscar filme')
    print('3- Atualizar dados do filme')
    print('4- Remover filme')
    print('5- Mostrar todos os filmes disponíveis')
    print('6- Mostrar ingressos vendidos de um filme específico')
    print('7- Gerar relatório de ingressos vendidos')
    print('0- Voltar')

def comprar_ingressos():
    print('\n---------------Comprar Ingressos---------------\n')
    print('Digite o nome do filme que deseja comprar ingressos ou 0 para voltar: ')
    filme_escolhido = input().strip()

    if filme_escolhido == '0':
        return

    if filme_escolhido in filmes:
        print(f'Informações sobre o filme "{filme_escolhido}":')
        print(f'Ano de lançamento: {filmes[filme_escolhido]["ano"]}')
        print(f'Diretor: {filmes[filme_escolhido]["diretor"]}')
        print(f'Salas de exibição: {filmes[filme_escolhido]["sala"]}')
        print(f'Lugares disponíveis: {filmes[filme_escolhido]["lugares"]}')
        print(f'Horários das sessões: {filmes[filme_escolhido]["horario"]}')
        print(f'Valor do ingresso: R$ {filmes[filme_escolhido]["valores"]:.2f}')

        confirmacao = input(f'Deseja comprar ingressos para o filme "{filme_escolhido}"? (sim/não): ').lower()

        if (confirmacao == 'sim'):
            qtde_ingressos = int(input('Quantos ingressos deseja comprar? '))
            if qtde_ingressos <= filmes[filme_escolhido]['lugares']:
                filmes[filme_escolhido]['lugares'] -= qtde_ingressos
                print(f'Compra efetuada com sucesso para o filme "{filme_escolhido}". Bom filme!')
                compra.append(filme_escolhido)
            else:
                print('Quantidade de ingressos desejada excede o número de lugares disponíveis.')
        elif (confirmacao == 'não'):
            print('Compra cancelada.')
        else:
            print('Opção inválida. Compra cancelada.')

    else:
        print(f'Filme "{filme_escolhido}" não encontrado.')


def ver_filmes_cartaz():
    print('\n---------------Filmes em Cartaz Esta Semana---------------\n')
    filmes_em_cartaz = False

    for filme, info in filmes.items():
        if (info.get('em_cartaz')):
            filmes_em_cartaz = True
            print(f'Filme: {filme}')
            print(f'Ano de lançamento: {info["ano"]}')
            print(f'Diretor: {info["diretor"]}')
            print(f'Salas de exibição: {info["sala"]}')
            print(f'Lugares disponíveis: {info["lugares"]}')
            print(f'Horários das sessões: {info["horario"]}')
            print(f'Valor do ingresso: R$ {info["valores"]:.2f}\n')

    if (not filmes_em_cartaz):
        print('Não há filmes em cartaz esta semana.')

    import re

def cadastrar_filme(filmes):
        print('\n---------------Cadastro de Novo Filme---------------\n')

        while True:
            filme = input('Digite o nome do filme: ').strip()
            if filme:
                break
            else:
                print('Erro! Nome do filme não pode ser vazio.')

        while True:
            idfilme = input('Digite o ID do filme: ')
            if idfilme.isdigit():
                idfilme = int(idfilme)
                break
            else:
                print('Erro! ID do filme deve ser um número.')

        while True:
            ano = input('Digite o ano de lançamento do filme: ')
            if ano.isdigit():
                ano = int(ano)
                break
            else:
                print('Erro! Ano de lançamento deve ser um número.')

        while True:
            diretor = input('Digite o nome do diretor do filme: ').strip()
            if diretor:
                break
            else:
                print('Erro! Nome do diretor não pode ser vazio.')

        while True:
            sala = input('Digite a sala de exibição do filme: ')
            if sala.isdigit():
                sala = int(sala)
                break
            else:
                print('Erro! Sala de exibição deve ser um número.')

        while True:
            lugares = input('Digite a quantidade de lugares disponíveis: ')
            if lugares.isdigit():
                lugares = int(lugares)
                break
            else:
                print('Erro! Quantidade de lugares deve ser um número.')

        horario = input('Digite o horário das sessões do filme: ')

        while True:
            valores = input('Digite o valor do ingresso para este filme: ')
            if re.match(r'^\d+(\.\d{1,2})?$', valores):
                valores = float(valores)
                break
            else:
                print('Erro! Valor do ingresso deve ser um número.')

        novo_filme = {
            'idfilme': idfilme,
            'ano': ano,
            'diretor': diretor,
            'sala': sala,
            'lugares': lugares,
            'horario': horario,
            'valores': valores,
            'em_cartaz': True
        }

        filmes.append(filmes)

        print(f'\nFilme cadastrado com sucesso!\n')


def buscar_filme(filmes):
    print('\n---------------Buscar Filme---------------\n')

    busca = input('Digite o nome do filme que deseja buscar: ')

    if busca in filmes:
        filme = filmes[busca]
        print('\n---------------Filme Encontrado---------------\n')
        print(f'Nome do Filme: {busca}')
        print(f'ID do Filme: {filme["idfilme"]}')
        print(f'Ano de Lançamento: {filme["ano"]}')
        print(f'Diretor: {filme["diretor"]}')
        print(f'Sala de Exibição: {filme["sala"]}')
        print(f'Lugares Disponíveis: {filme["lugares"]}')
        print(f'Horários das Sessões: {filme["horario"]}')
        print(f'Valor do Ingresso: R$ {filme["valores"]:.2f}')
    else:
        print(f'\nFilme "{busca}" não encontrado.')

    return filmes



def atualizar_filme(filmes):
    print('\n---------------Atualizar Dados do Filme---------------\n')

    busca = input('Digite o nome do filme que deseja atualizar: ')

    if busca in filmes:
        filme = filmes[busca]

        print(f'\nFilme "{busca}" encontrado. Informe os novos dados:\n')

        filme['nome'] = input('Nome do filme: ')
        filme['idfilme'] = int(input('ID do filme: '))
        filme['ano'] = int(input('Ano de lançamento: '))
        filme['diretor'] = input('Diretor(a): ')
        filme['sala'] = int(input('Salas de exibição: '))
        filme['lugares'] = int(input('Lugares disponíveis: '))
        filme['horario'] = input('Horários das sessões: ')
        filme['valores'] = float(input('Valor do ingresso: R$ '))

        print(f'\nFilme "{busca}" atualizado com sucesso!\n')
    else:
        print(f'\nFilme "{busca}" não encontrado.\n')

    return filmes


def remover_filme(filmes):
    print('\n---------------Remover Filme---------------\n')

    busca = input('Digite o nome do filme que deseja remover: ')

    if (busca in filmes):
        confirmacao = input(f'Tem certeza que deseja remover o filme "{busca}"? (sim/não): ')
        if (confirmacao.lower() == 'sim'):
            del filmes[busca]
            print(f'\nFilme "{busca}" removido com sucesso!\n')
        else:
            print(f'\nOperação de remoção cancelada para o filme "{busca}".\n')
    else:
        print(f'\nFilme "{busca}" não encontrado.\n')

    return filmes


def mostrar_filmes(filmes):
    print('\n---------------Todos os Filmes Disponíveis---------------\n')

    if not filmes:
        print('Não há filmes cadastrados.')
    else:
        if isinstance(filmes, dict):
            for chave, filme in filmes.items():
                print(f'Nome do Filme: {chave}')
                print(f'ID do Filme: {filme["idfilme"]}')
                print(f'Ano de Lançamento: {filme["ano"]}')
                print(f'Diretor(a): {filme["diretor"]}')
                print(f'Salas de Exibição: {filme["sala"]}')
                print(f'Lugares Disponíveis: {filme["lugares"]}')
                print(f'Horários das Sessões: {filme["horario"]}')
                print(f'Valor do Ingresso: R$ {filme["valores"]:.2f}')
                print(f'Ingressos Vendidos: {filme.get("ingressosvendidos", 0)}')
        else:
            print('Formato de dados inválido para filmes.')

    input('\nPressione Enter para continuar...')



def mostrar_ingressos_vendidos(compra):
    print('\n---------------Todos os Ingressos Vendidos---------------\n')

    if (not compra):
        print('Não há ingressos vendidos registrados.')
    else:
        for ingresso in compra:
            print(f'Ingresso: {ingresso}')

    input('\nPressione Enter para continuar...')


def mostrar_ingressos_filme(filmes):
    print('\n---------------Ingressos Vendidos para um Filme Específico---------------\n')


    nome_filme = input('Digite o nome do filme para ver os ingressos vendidos: ')


    filme = filmes.get(nome_filme)

    if (filme):
        ingressos_vendidos = filme.get('ingressos_vendidos', 0)
        print(f'Filme: {nome_filme}')
        print(f'Ingressos Vendidos: {ingressos_vendidos}')
    else:
        print(f'O filme "{nome_filme}" não foi encontrado.')

    input('\nPressione Enter para continuar...')


def gerar_relatorio(ingressos_vendidos):
    print('\n---------------Gerar Relatório de Ingressos Vendidos---------------\n')


    if (not ingressos_vendidos):
        print('Não há ingressos vendidos para gerar relatório.')
        return

    nome_arquivo = 'relatorio_ingressos_vendidos.txt'

    try:
        with open(nome_arquivo, 'w') as arquivo:

            arquivo.write('Relatório de Ingressos Vendidos\n\n')


            for filme, qtde_ingressos in ingressos_vendidos.items():
                arquivo.write(f'Filme: {filme}\n')
                arquivo.write(f'Ingressos Vendidos: {qtde_ingressos}\n')
                arquivo.write('-' * 30 + '\n')

        print(f'Relatório gerado com sucesso em {nome_arquivo}')
    except IOError:
        print(f'Erro ao gerar relatório em {nome_arquivo}')

    input('\nPressione Enter para continuar...')


def alterar_dados_admin(usuarios):
    print('\n---------------Alterar Dados Cadastrais do Administrador---------------\n')

    login = input('Digite o login do administrador que deseja alterar os dados: ')

    if (login in usuarios and usuarios[login][1] == 1):  # Verifica se o login existe e se é um administrador (perfil 1)
        print('Opções disponíveis para alteração:')
        print('1 - Alterar login')
        print('2 - Alterar senha')
        print('3 - Alterar email')
        print('4 - Voltar ao menu anterior')

        opcao = input('Digite o número da opção desejada: ')

        if (opcao == '1'):
            novo_login = input('Digite o novo login: ')
            usuarios[login][0] = novo_login
            print('Login atualizado com sucesso!')
        elif (opcao == '2'):
            nova_senha = input('Digite a nova senha: ')
            usuarios[login][2] = nova_senha
            print('Senha atualizada com sucesso!')
        elif (opcao == '3'):
            novo_email = input('Digite o novo email: ')
            usuarios[login][3] = novo_email
            print('Email atualizado com sucesso!')
        elif (opcao == '4'):
            print('Operação cancelada. Retornando ao menu anterior...')
        else:
            print('Opção inválida. Tente novamente.')

    else:
        print('Login de administrador não encontrado.')

    input('\nPressione Enter para continuar...')

def ver_filmes_disponiveis(filmes):
    print('\n---------------Ver Filmes Disponíveis---------------\n')

    if (not filmes):
        print('Nenhum filme cadastrado.')
    else:
        for chave, filme in filmes.items():
            print(f'Filme: {chave}')
            print(f'ID: {filme["idfilme"]}')
            print(f'Ano de Lançamento: {filme["ano"]}')
            print(f'Diretor: {filme["diretor"]}')
            print(f'Salas de Exibição: {filme["sala"]}')
            print(f'Lugares Disponíveis: {filme["lugares"]}')
            print(f'Horários das Sessões: {filme["horario"]}')
            print(f'Valor do Ingresso: R$ {filme["valores"]:.2f}')
            print(f'Ingressos Vendidos: {filme["ingressosvendidos"]}')
            print('-----------------------------------')

    input('\nPressione Enter para continuar...')


def ver_minhas_compras(compras):
    print('\n---------------Ver Minhas Compras---------------\n')

    if (not compras):
        print('Você ainda não realizou nenhuma compra.')
    else:
        for compra in compras:
            print(f'Filme: {compra["nome_filme"]}')
            print(f'ID do Filme: {compra["id_filme"]}')
            print(f'Quantidade de Ingressos: {compra["quantidade"]}')
            print(f'Data da Compra: {compra["data_compra"]}')
            print('-----------------------------------')

    input('\nPressione Enter para continuar...')

def alterar_dados_cliente(usuarios):
    print('\n---------------Alterar Dados Cadastrais do Cliente---------------\n')

    login = input('Digite o login do administrador que deseja alterar os dados: ')

    if (login in usuarios and usuarios[login][1] == 2):
        print('Opções disponíveis para alteração:')
        print('1 - Alterar login')
        print('2 - Alterar senha')
        print('3 - Alterar email')
        print('4 - Voltar ao menu anterior')

        opcao = input('Digite o número da opção desejada: ')

        if (opcao == '1'):
            novo_login = input('Digite o novo login: ')
            usuarios[login][0] = novo_login
            print('Login atualizado com sucesso!')
        elif (opcao == '2'):
            nova_senha = input('Digite a nova senha: ')
            usuarios[login][2] = nova_senha
            print('Senha atualizada com sucesso!')
        elif (opcao == '3'):
            novo_email = input('Digite o novo email: ')
            usuarios[login][3] = novo_email
            print('Email atualizado com sucesso!')
        elif (opcao == '4'):
            print('Operação cancelada. Retornando ao menu anterior...')
        else:
            print('Opção inválida. Tente novamente.')

    else:
        print('Login de Cliente não encontrado.')

    input('\nPressione Enter para continuar...')


def cancelar_compra(compras):
    print('\n---------------Cancelar Compra---------------\n')

    if (not compras):
        print('Não há compras registradas para cancelar.\n')
        return


    print('Compras registradas:')
    for idx, compra in enumerate(compras, start=1):
        print(f'{idx}. {compra}')


    while True:
        try:
            num_compra = int(input('Digite o número da compra que deseja cancelar (ou 0 para voltar): '))
            if (num_compra == 0):
                print('Cancelamento de compra finalizado.\n')
                break
            elif (1 <= num_compra <= len(compras)):
                compra_cancelada = compras.pop(num_compra - 1)
                print(f'Compra "{compra_cancelada}" cancelada com sucesso.\n')
                break
            else:
                print('Número de compra inválido. Digite um número válido ou 0 para voltar.\n')
        except ValueError:
            print('Por favor, digite um número válido.\n')

    input('Pressione Enter para continuar...')