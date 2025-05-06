import os
import shutil as st
global dados
global last_backup_id


def gravar(**kargs):
    with open('database/data.txt', 'w') as f:
        for chave, valor in kargs.items():
            valor = str(valor).strip()
            f.write(f'{chave}={valor}\n')


def save():
    global dados, last_backup_id
    last_backup_id = get_id()
    gravar(kwh=dados['kwh'], agua=dados['agua'], internet=dados['internet'], ht=dados['ht'], custo=dados['custo'])
    backup(f'database/backup{last_backup_id + 1}.txt')


def ler():
    global dados
    dados = {}
    with open('database/data.txt', 'r') as f:
        for linha in f:
            chave, valor = [p.strip() for p in linha.replace('\n', '').split('=')]
            dados[chave] = float(valor)
    return dados


def get_id():
    with open('database/id_registry.txt', 'r') as f:
        ids = []
        for x in f:
            ids.append(int(x))
        return ids[0]


def store_id():
    global last_backup_id
    with open('database/id_registry.txt', 'w') as f:
        f.write(str(last_backup_id))


def mostrar_menu(opcoes):
    for opcao, descricao in opcoes.items():
        print(f'{opcao} - {descricao}')


def chose(txt, opcoes):
    while True:
        entrada = input(txt).strip().lower()
        if entrada in opcoes:
            break
        else:
            print('ERRO: Opção Inexinstente')
    return entrada


def insert_float(txt):
    while True:
        entrada = input(txt).replace(',', '.').strip()
        try:
            x = float(entrada)
            break
        except ValueError:
            print('ERRO: entrada inválida')
            print('DICA: insira apenas números')
    return x


def calc_custo():
    global dados
    dados['custo'] = dados['kwh'] * dados['ht']
    dados['custo'] += dados['internet'] / 30 / 24 * dados['ht']
    dados['agua'] = round(dados['kwh'] * 0.1, 2)
    dados['custo'] += dados['agua']
    dados['custo'] = round(dados['custo'], 2)


def mostrar_dados():
    for key, value in dados.items():
        print(f'{key} = {value}')


def wipe_data():
    global last_backup_id
    last_backup_id = get_id()
    st.copy('database/data.txt', f'database/backup{last_backup_id + 1}.txt')
    last_backup_id += 1
    store_id()
    gravar(kwh=0, agua=0, internet=0, ht=0, custo=0)
    global dados
    dados = ler()


def alterar_kwh():
    dados['kwh'] = insert_float('\nInsira o novo valor do kW/h em Reais: ')


def alterar_internet():
    dados['internet'] = insert_float('\nInsira o preço mensal do plano de Internet em Reais: ')


def adicionar_ht():
    dados['ht'] += insert_float('\nInsira quantas horas você quer adicionar: ')


def truncate():
    global last_backup_id
    for i in range(last_backup_id):
        try:
            os.remove(f'database/backup{i + 1}.txt')
        except FileNotFoundError:
            pass
    last_backup_id = 0
    store_id()
    last_backup_id = get_id()


def show_data(local):
    if local == 'none':
        print('\nNão há Backups no momento')
    else:
        with open(local, 'r') as f:
            print('\n')
            for line in f:
                print(line.replace('\n', '').replace('=', ' = '))
            print('\n')


def backup(local):
    global last_backup_id
    last_backup_id = get_id() + 1
    st.copy('database/data.txt', local)
    store_id()


def reformat():
    truncate()
    st.copy('database/origin.txt', 'database/data.txt')


def terminal():
    global dados
    global last_backup_id
    last_backup_id = get_id()
    remain = True
    while remain:
        command = input('\n>>> ')
        commands = {
            'restore': lambda: st.copy(f'database/backup{last_backup_id}.txt', 'database/data.txt'),
            'restore from origin': lambda: st.copy('database/origin.txt', 'database/data.txt'),
            'truncate': truncate,
            'bin': lambda: print(str(list(commands.keys())).replace(']', '') + ", 'exit']"),
            'show local data': lambda: show_data('database/data.txt'),
            'show origin data': lambda: show_data('database/origin.txt'),
            'show backup data': lambda: show_data(
                f'database/backup{last_backup_id}.txt' if last_backup_id != 0 else 'none'),
            'show backup id': lambda: show_data('database/id_registry.txt'),
            'wipe': lambda: wipe_data(),
            'backup': lambda: backup(f'database/backup{last_backup_id + 1}.txt'),
            'backup to origin': lambda: backup('database/origin.txt'),
            'reformat': reformat,
        }

        if command in commands.keys():
            commands[command]()
        elif command == 'exit':
            break
        else:
            print('Comando não reconhecido')

        dados = ler()
        save()
