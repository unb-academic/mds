# MDS - Squad 06 (2023/2)

Repositório contendo o código do projeto da disciplina de Métodos de
Desenvolvimento de Software. O projeto consiste em um juíz online para
programação competitiva.

## Membros

| Nome             | Matrícula | GitHub |
|------------------|-----------|--------|
| Caio Alexandre   | 221007644 | [@bitterteriyaki](https://github.com/bitterteriyaki) |
| João Farias      | 221008187 | [@jpcfarias](https://github.com/jpcfarias) |
| Gabriel Moura    | 221008060 | [@thegm445](https://github.com/thegm445) |
| Luiza Maluf      | 221008294 | [@LuizaMaluf](https://github.com/LuizaMaluf) |
| Letícia Hladczuk | 221039209 | [@HladczukLe](https://github.com/HladczukLe) |
| Esther Silva     | 190106034 | [@EstherSousa](https://github.com/EstherSousa) |
| Gabriel Fernando | 222022162 | [@MMcLovin](https://github.com/MMcLovin) |

## Instalação

### Ambiente

Recomendamos o uso de **distribuições baseadas em Debian** como ambiente de
desenvolvimento do projeto. No Windows, recomendamos o uso do [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

### Começando

Você pode instalar o projeto com os seguintes comandos:

```bash
# Clonando o repositório do projeto:
$ git clone https://github.com/unb-mds/2023-2-Squad06.git
# Entrando na pasta do projeto:
$ cd 2023-2-Squad06
```

Tendo feito isso, instale as dependências do projeto com o Poetry:

```bash
$ poetry install
# Caso você precise das dependências de documentação, use:
$ poetry install --with docs
```

Crie o arquivo de ambiente usando o script do próprio projeto:

```bash
$ poetry run ./bin/create-env
```

Por fim, rode o projeto com o Docker:

```bash
$ docker compose up # para rodar em segundo plano, adicione ' -d '
```

Para rodar as migrações do banco de dados, você precisará criar um container
temporário que executará as migrações. Faça isso com o seguinte comando:

```bash
$ docker compose run --rm web python manage.py migrate
```

Para fechar o servidor do Django, use o seguinte comando:

```bash
$ docker compose down
# Caso você queira remover os volumes do Docker, use:
$ docker compose down -v
# Isto removerá os volumes do Docker, o que significa que os dados do banco de dados serão perdidos.
```

Em caso de problemas com a instalação, verifique a
[documentação](https://mds-squad-06.readthedocs.io/pt/latest/installation.html).

## Links

- [Documentação](https://mds.kyomi.dev/pt/latest/)
