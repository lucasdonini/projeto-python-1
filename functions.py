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
    while True:
        try:
            gravar(kwh=dados['kwh'], agua=dados['agua'], internet=dados['internet'], ht=dados['ht'], custo=dados['custo'])
            break
        except KeyError:
            dados = ler()
        except Exception as e:
            print(f'Erro inesperado: {e}')
    backup(f'database/backup{last_backup_id + 1}.txt')


def ler():
    global dados
    dados = {'kwh': 0, 'agua': 0, 'internet': 0, 'ht': 0, 'custo': 0}
    with open('database/data.txt', 'r') as f:
        for linha in f:
            chave, valor = [p.strip() for p in linha.replace('\n', '').split('=')]
            dados[chave] = float(valor)
    return dados


def get_id():
    try:
        with open('database/id_registry.txt', 'r') as f:
            return int(f.read().strip())  # Convertendo para int e removendo espaços em branco
    except (FileNotFoundError, ValueError):
        return 0  # Retorna 0 se o arquivo não existir ou se houver erro na conversão


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
    limit_backup()


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
            'repair': init,
            'set backup limit':lambda: set_backup_limit(input('>>> New Limit: '))
        }

        if command in commands.keys():
            commands[command]()
        elif command == 'exit':
            break
        else:
            print('Comando não reconhecido')

        dados = ler()
        save()


def init():
    if os.path.exists('database'):
        pass
    else:
        os.mkdir('database')

    gravar(kwh=0, agua=0, internet=0, ht=0, custo=0)

    with open('database/id_registry.txt', 'w') as f:
        f.write('0')

    with open('database/origin.txt', 'w') as f:
        pass

    backup('database/origin.txt')

    set_backup_limit('10')

    truncate()


def limit_backup():
    global last_backup_id
    last_backup_id = get_id()
    backup_ids = [x for x in range(1, last_backup_id+1) if x > 0][:-get_backup_limit()]
    for i in backup_ids:
        try:
            os.remove(f'database/backup{i}.txt')
        except:
            pass


def get_backup_limit():
    try:
        with open('database/backup_limit.txt', 'r') as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        set_backup_limit(10)
        return 10


def set_backup_limit(x):
    x = x.strip()
    if not x.isdigit():
        print('ERRO: valor inválido')
    else:
        with open('database/backup_limit.txt', 'w') as f:
            f.write(x)