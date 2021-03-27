# FSL

Rede social corporativa para compartilhar filmes, séries e livros entre colaboradores.

## Dependências

- [Python](https://www.python.org/downloads/) - Versão 3.5+
- [django](http://www.djangoproject.com) == 3.1.7


## Como rodar o projeto?

- Clone este repositório.
- Crie um virtualenv com python 3.
- Ative o virtualenv.
- Instale as dependências.

```bash
git clone https://github.com/fgmw-adsMack/App_FSL.git
cd App_FSL
python3 -m venv .fsl
source .fsl/bin/activate
pip install -r requirements.t
```

- Crie um .env com as variáveis de ambiente, considerando:

```bash
cat << EOF > .env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=127.0.0.1,.localhost
EOF
```

- Rode as migrações:

```bash
python manage.py migrate
```

- Crie um usuário (Administrador do sistema):

```bash
python manage.py createsuperuser
```

- Teste a instalação carregando o servidor de desenvolvimento:

```bash
python manage.py runserver
```

## Documentação

Accese na [Wiki](https://github.com/fgmw-adsMack/App_FSL/wiki) do projeto.
