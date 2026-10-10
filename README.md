
# TaskForge

Gerenciador de tarefas desenvolvido em Python, com interface de linha de comando (CLI) e persistência de dados em PostgreSQL.

O projeto foi criado para colocar em prática conhecimentos de programação, SQL e integração entre aplicações Python e bancos de dados relacionais.

## Funcionalidades

- Listar tarefas cadastradas
- Adicionar novas tarefas
- Remover tarefas pelo título
- Marcar tarefas como concluídas
- Definir prioridades
- Armazenar os dados no PostgreSQL

## Tecnologias

- Python 3
- PostgreSQL
- Psycopg 3
- Python-dotenv
- SQL
- Git e GitHub

## Estrutura do projeto

```text
TaskForge/
├── database/
│   └── connection.py
├── task/
│   ├── tarefa.py
│   └── task_service.py
├── menu.py
├── .env
├── .gitignore
└── README.md
```

## Banco de dados

O TaskForge utiliza uma tabela chamada `tarefas`:

```sql
CREATE TABLE tarefas (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    prioridade VARCHAR(20) NOT NULL,
    concluida BOOLEAN DEFAULT FALSE
);
```

As operações são realizadas utilizando comandos SQL parametrizados, evitando a concatenação direta de valores nas consultas.

## Configuração

1. Clone o repositório:

```bash
git clone https://github.com/Mutus142/TaskForge.git
cd TaskForge
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install "psycopg[binary]" python-dotenv
```

4. Configure o PostgreSQL com o banco `TaskForge`, a tabela `tarefas` e um usuário com as permissões necessárias.

5. Crie um arquivo `.env` na raiz do projeto:

```env
TASKFORGE_DB_PASSWORD=sua_senha
```

A configuração de host, porta, banco e usuário está no arquivo `database/connection.py`.

## Desenvolvimento

O projeto começou com a implementação de operações CRUD utilizando Python e PostgreSQL.

A primeira versão contempla o gerenciamento básico de tarefas. Melhorias previstas incluem:

- Remoção e atualização por ID
- Validação de títulos e prioridades
- Tratamento de erros de banco de dados
- Melhorias na interface do terminal
- Organização e testes do código

## Autor

**Mateus Ribeiro Simão**

GitHub: https://github.com/Mutus142
