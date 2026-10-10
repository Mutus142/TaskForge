<div align="center">

# ⚒️ TaskForge

### Gerenciador de tarefas em Python com persistência de dados no PostgreSQL

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-openSUSE-73BA25?style=for-the-badge&logo=opensuse&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.0-8A2BE2?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-22C55E?style=for-the-badge)

**Uma aplicação CLI para cadastrar, consultar, remover e concluir tarefas, utilizando Python e PostgreSQL.**

[Sobre](#-sobre-o-projeto) •
[Funcionalidades](#-funcionalidades) •
[Tecnologias](#️-tecnologias-utilizadas) •
[Instalação](#-instalação) •
[Próximas versões](#-próximas-funcionalidades)

</div>

---

## 📌 Sobre o projeto

O **TaskForge** é um gerenciador de tarefas executado pelo terminal, desenvolvido em **Python** com armazenamento persistente em **PostgreSQL**.

O projeto nasceu como uma forma de praticar a integração entre aplicações Python e bancos de dados relacionais, aplicando comandos SQL, organização modular e operações **CRUD** (*Create, Read, Update e Delete*).

Cada tarefa possui um identificador, título, prioridade e situação de conclusão. Os registros ficam armazenados no banco de dados, mesmo após o encerramento da aplicação.

---

## 🚀 Funcionalidades

| Operação | Funcionalidade | SQL |
|:---|:---|:---:|
| 📋 **Visualizar tarefas** | Lista os registros, exibindo ID, título, prioridade e situação | `SELECT` |
| ➕ **Adicionar tarefa** | Cadastra uma tarefa com título e prioridade | `INSERT` |
| 🗑️ **Remover tarefa** | Exclui tarefas a partir do título informado | `DELETE` |
| ✅ **Concluir tarefa** | Atualiza a situação da tarefa para concluída | `UPDATE` |
| 💾 **Persistência** | Mantém os registros armazenados no PostgreSQL | — |

### ⚙️ Recursos adicionais

- Interface textual com cabeçalhos e separadores padronizados.
- Exibição de tarefas **pendentes** e **concluídas**.
- Identificadores gerados automaticamente pelo banco de dados.
- Conexão com PostgreSQL por meio da biblioteca `psycopg`.
- Consultas SQL parametrizadas com `%s`.
- Senha de acesso ao banco carregada de uma variável de ambiente.
- Separação entre a configuração de conexão e as operações sobre tarefas.

> [!IMPORTANT]
> Nesta versão, as operações de remoção e conclusão utilizam o **título** da tarefa. Se houver títulos repetidos, mais de um registro poderá ser afetado. A migração dessas operações para **ID** está prevista para uma próxima atualização.

---

## 🛠️ Tecnologias utilizadas

<div align="center">

| Tecnologia | Utilização |
|:---:|:---|
| **Python 3** | Lógica da aplicação e interface de terminal |
| **PostgreSQL** | Armazenamento relacional das tarefas |
| **Psycopg 3** | Comunicação entre Python e PostgreSQL |
| **python-dotenv** | Carregamento das variáveis do arquivo `.env` |
| **SQL** | Operações `SELECT`, `INSERT`, `UPDATE` e `DELETE` |
| **Linux / openSUSE** | Ambiente de desenvolvimento |
| **Git** | Controle de versão |
| **GitHub** | Hospedagem do código e documentação |
| **VS Code** | Edição e desenvolvimento do projeto |

</div>

### 🐍 Python e PostgreSQL

O **Python** é responsável por receber as entradas do usuário, executar a lógica das funções e apresentar os resultados no terminal.

O **PostgreSQL** armazena as tarefas em uma tabela relacional. A biblioteca **Psycopg 3** permite executar os comandos SQL diretamente pelo Python, utilizando parâmetros para transmitir os valores com segurança.

O **python-dotenv** permite carregar a senha de conexão a partir de um arquivo local `.env`, evitando colocá-la diretamente no código-fonte.

---

## 📂 Estrutura do projeto

```text
TaskForge/
│
├── menu.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env                 # Arquivo local, não versionado
│
├── database/
│   └── connection.py
│
└── task/
    ├── tarefa.py
    └── task_service.py
```

O arquivo `database/connection.py` concentra a configuração da conexão com o PostgreSQL.

O módulo `task/task_service.py` contém as funções responsáveis pelas operações sobre as tarefas.

O arquivo `task/tarefa.py` é destinado à representação de uma tarefa em Python.

O arquivo `menu.py` é o ponto previsto para reunir a navegação entre as funcionalidades da aplicação.

---

## 🗄️ Estrutura do banco de dados

A aplicação utiliza o banco de dados **`TaskForge`** e a tabela **`tarefas`**.

```sql
CREATE TABLE tarefas (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    prioridade VARCHAR(20) NOT NULL,
    concluida BOOLEAN DEFAULT FALSE
);
```

| Coluna | Tipo | Descrição |
|:---|:---|:---|
| `id` | `INTEGER` | Identificador gerado automaticamente |
| `titulo` | `VARCHAR(150)` | Nome da tarefa |
| `prioridade` | `VARCHAR(20)` | Prioridade informada pelo usuário |
| `concluida` | `BOOLEAN` | `FALSE` para pendente e `TRUE` para concluída |

---

## 🖥️ Prévia do sistema

### 📋 Listagem de tarefas

Exemplo ilustrativo da saída no terminal:

```text
========== TASKFORGE ==========
         SUAS TAREFAS
===============================

ID:         1
Título:     Estudar Python
Prioridade: Alta
Situação:   Pendente
-------------------------------

ID:         5
Título:     teste
Prioridade: teste
Situação:   Concluída
-------------------------------
===============================
```

### ➕ Cadastro de tarefa

```text
========== TASKFORGE ==========
       ADICIONAR TAREFA
===============================
Qual é o título? Estudar PostgreSQL
Qual é a prioridade? Alta

-------------------------------
  Tarefa adicionada com sucesso!
  Título: Estudar PostgreSQL
  Prioridade: Alta
===============================
```

### 🗑️ Remoção de tarefa

```text
========== TASKFORGE ==========
         REMOVER TAREFA
===============================

Título da tarefa: Estudar PostgreSQL

-------------------------------
  Tarefa removida com sucesso!
  Título: Estudar PostgreSQL
===============================
```

### ✅ Conclusão de tarefa

```text
========== TASKFORGE ==========
         CONCLUIR TAREFA
===============================
Qual é a tarefa que deseja concluir? Estudar Python

-------------------------------
  Tarefa concluída com sucesso!
  Título: Estudar Python
===============================
```

---

## 📥 Instalação

### 1. Pré-requisitos

- Python 3 instalado.
- PostgreSQL instalado e em execução.
- Git para clonar o repositório.

### 2. Clone o repositório

```bash
git clone https://github.com/Mutus142/TaskForge.git
cd TaskForge
```

### 3. Crie e ative o ambiente virtual

No Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
python -m pip install "psycopg[binary]" python-dotenv
```

### 5. Configure o PostgreSQL

Crie o banco de dados chamado **`TaskForge`**, execute o SQL apresentado na seção [Estrutura do banco de dados](#️-estrutura-do-banco-de-dados) e configure um usuário com permissão para consultar e modificar os registros da tabela.

A conexão atualmente utiliza as seguintes configurações:

```python
host="localhost"
port=5432
dbname="TaskForge"
user="taskforge_user"
```

> [!NOTE]
> O PostgreSQL diferencia maiúsculas de minúsculas em nomes criados entre aspas. Ao criar o banco com letras maiúsculas, preserve o nome `"TaskForge"`.

### 6. Configure a variável de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
TASKFORGE_DB_PASSWORD=sua_senha_aqui
```

> [!CAUTION]
> Nunca publique o arquivo `.env` com senhas reais. Confirme que ele está listado no `.gitignore`.

### 7. Execute as funcionalidades

Na raiz do projeto, com o ambiente virtual ativado:

**Visualizar tarefas:**

```bash
python -c "from task.task_service import ver_task; ver_task()"
```

**Adicionar tarefa:**

```bash
python -c "from task.task_service import adicionar_task; adicionar_task()"
```

**Remover tarefa:**

```bash
python -c "from task.task_service import remove_task; remove_task()"
```

**Concluir tarefa:**

```bash
python -c "from task.task_service import concluir_task; concluir_task()"
```

> [!NOTE]
> Esses comandos executam as funções diretamente. A integração completa com o menu principal deve ser confirmada antes de documentar `python menu.py` como entrada oficial da aplicação.

---

## 📝 Histórico de versões

### 🔵 V1.0 — CRUD com PostgreSQL

- Criação da estrutura inicial do projeto.
- Configuração da conexão entre Python e PostgreSQL.
- Implementação da tabela de tarefas com ID automático.
- Cadastro de tarefas utilizando `INSERT`.
- Consulta e exibição formatada com `SELECT`.
- Remoção de tarefas utilizando `DELETE`.
- Conclusão de tarefas utilizando `UPDATE`.
- Uso de parâmetros SQL e variáveis de ambiente.
- Padronização da saída no terminal.

---

## 🔮 Próximas funcionalidades

- [ ] Remover e concluir tarefas pelo **ID**.
- [ ] Validar as opções de prioridade.
- [ ] Impedir o cadastro de títulos vazios.
- [ ] Identificar tarefas já concluídas.
- [ ] Integrar e testar todas as operações pelo menu principal.
- [ ] Melhorar o tratamento de exceções e erros de conexão.
- [ ] Adicionar filtros por prioridade e situação.
- [ ] Permitir editar títulos e prioridades.
- [ ] Criar testes automatizados.

---

## 👨‍💻 Desenvolvedor

<div align="center">

### Mateus — Mutus142

Projeto desenvolvido para aprimorar conhecimentos em **Python, SQL, PostgreSQL e desenvolvimento de aplicações com banco de dados**.

[![GitHub](https://img.shields.io/badge/GitHub-Mutus142-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mutus142)

**⭐ Se gostou do projeto, considere deixar uma estrela no repositório!**

</div>
