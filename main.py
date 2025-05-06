from functions import *

# leitura do banco de dados e criação dos dados temporarios
try:
    dados = ler()
except ValueError:
    print('ERRO: Algo deu errado ao carregar os dados')
    terminal()

# Menu e suas funções
opcoes_menu = {
    '0': 'Salvar e Sair',
    '1': 'Alterar Valor do kW/h',
    '2': 'Alterar valor do plano de Internet',
    '3': 'Adicionar Horas Trabalhadas',
    '*': 'Terminal'
}

funcoes_menu = {
    'Salvar e Sair': lambda: None,
    'Alterar Valor do kW/h': alterar_kwh,
    'Alterar valor do plano de Internet': alterar_internet,
    'Adicionar Horas Trabalhadas': adicionar_ht,
    'Terminal': terminal
}

# variáveis auxiliares
last_backup_id = get_id()


def main():
    while True:
        os.system('cls')
        mostrar_menu(opcoes_menu)

        escolha = chose('\nInsira o número correspondente a sua escolha: ', opcoes_menu.keys())
        funcoes_menu[opcoes_menu[escolha]]()

        calc_custo()
        save()

        print('\nDADOS SALVOS:')
        mostrar_dados()

        opcao_saida = [chave for chave, valor in opcoes_menu.items() if valor == 'Salvar e Sair']
        if escolha in opcao_saida: break

        input('\nPressione [enter] para voltar ao Menu')


if __name__ == '__main__': main()
