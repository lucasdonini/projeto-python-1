# projeto-python-1
## Organização dos branches do Repositório Remoto:
* O branch main é reservado para os arquivos de organização relacionados às licenças e para o README.md
* O branch master, por sua vez, é o que contém os arquivos do programa mesmo

## Instruções de clonagem:
Use: `git clone -b master 'https://github.com/lucasdonini/projeto-python-1' <nome do diretório de sua escolha>`

## Requisitos de Funcionamento:
* Criar um diretório chamado 'database'
* Criar o arquivo database/origin.txt
* Criar o arquivo database/data.txt
* Usar um ambiente virtual compatível

## Módulos Importados
* shutil
* os

## Primeiros Passos
1. Preencha o arquivo origin.txt com dados seguindo o modelo abaixo:
    ```
    kwh=0
    agua=0
    internet=0
    ht=0
    custo=0
    ```
2. Rode o Main.
3. Use os comandos do menu para alterar seus dados da maneira que preferir

## Comandos do Terminal:
* `bin`: exibe os comandos existentes
* `restore`: restaura os dados do último backup
* `restore from origin`: restaura os dados da orígem (`origin.txt`)
* `truncate`: apaga todos os backups, mas matém a origem inalterada
* `show local data`: mostra os dados de `data.txt`
* `show origin data`: mostra os dados da orígem (`origin.txt`)
* `show backup data`: mostra os dados do último backup
* `show backup id`: mostra o id do último backup. Ex.: o id de `backup25.txt` é 25
* `wipe`: salva todos os dados como 0, mas cria um backup com as últimas informações
* `backup`: salva os dados locais (`data.txt`) em um arquivo de backup
* `backup to origin`: salva os dados locais (`data.txt`) na orígem (`origin.txt`)
* `reformat`: limpa os backups, limpa os dados locais e restaura da orígem
* `exit`: sai do terminal

# !!!AINDA NÃO CONLCUIDO. NÃO USE O PROGRAMA AINDA!!!
