# projeto-python-1
## Organização dos branches do Repositório Remoto:
* O branch main é reservado para os arquivos de organização relacionados às licenças e para o README.md
* O branch master, por sua vez, é o que contém os arquivos do programa mesmo

## Instruções de clonagem e utilização do programa:
* Use `git clone -b master 'https://github.com/lucasdonini/projeto-python-1' <nome do diretório de sua escolha>` para clonar o diretório
* Use um ambiente virtual compatível
* Crie um atalho para o acrivate.bat na área de trabalho ou outro lugar de sua peferência (opcional)
* Também disponibilizei um png com a logo do python, você pode usar como ícone do atalho (opcional)


## Módulos Importados
* shutil
* os

## Primeiros Passos
1. Rode activate.bat.
2. Use os comandos do menu para alterar seus dados da maneira que preferir

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
* `repair`: repara toda a estrutura de dados necessária para o programa funcionar dentro de uma pasta chamada `database`. Também apaga TODAS as informações.
* `set backup limit`: pede um input de um número inteiro positivo que será o limite de arquivos de backup. O valor padrão é 10


> Contato: se você não tem, problema seu. Não vou por aqui

> Caso encotre algum erro ou tenha alguma sugestão, entre em contato comigo.
