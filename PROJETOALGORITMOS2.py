import funcionalidadescinema as fun
from funcionalidadescinema import *

usuarios = {}
filmes = []
compra = []

while True:
    fun.exibir_menu_principal()
    opcao = input('Escolha uma opção: ').strip()

    if (opcao == '1'):
        fun.cadastrar_usuario(usuarios)

    elif (opcao == '2'):
        perfil = fun.login_usuario(usuarios)
        if (perfil == 1):
            while True:
                fun.exibir_menu_adm()
                opcao_adm = input('Escolha uma opção: ').strip()
                if (opcao_adm == '1'):
                    fun.cadastrar_filme(filmes)
                elif (opcao_adm == '2'):
                    fun.buscar_filme(filmes)
                elif (opcao_adm == '3'):
                    fun.atualizar_filme(filmes)
                elif (opcao_adm == '4'):
                    fun.remover_filme(filmes)
                elif (opcao_adm == '5'):
                    fun.mostrar_filmes(filmes)
                elif (opcao_adm == '6'):
                    fun.mostrar_ingressos_vendidos(compra)
                elif (opcao_adm == '7'):
                    fun.mostrar_ingressos_filme(filmes)
                elif (opcao_adm == '8'):
                    fun.alterar_dados_admin(usuarios)
                elif (opcao_adm == '0'):
                    break
                else:
                    print('Opção inválida. Tente novamente.')

        elif (perfil == 2):
            while True:
                fun.exibir_menu_cliente()
                opcao_cliente = input('Escolha uma opção: ').strip()
                if (opcao_cliente == '1'):
                    fun.comprar_ingressos(filmes, compra)
                elif (opcao_cliente == '2'):
                    fun.ver_filmes_disponiveis(filmes)
                elif (opcao_cliente == '3'):
                    fun.ver_minhas_compras(compra)
                elif (opcao_cliente == '4'):
                    fun.alterar_dados_cliente(usuarios)
                elif (opcao_cliente == '5'):
                    fun.cancelar_compra(compra)
                elif (opcao_cliente == '0'):
                    break
                else:
                    print('Opção inválida. Tente novamente.')

    elif (opcao == '3'):
        fun.ver_filmes_cartaz(filmes)

    elif (opcao == '0'):
        print('Saindo do sistema. Até mais!')
        break

    else:
        print('Opção inválida. Tente novamente.')