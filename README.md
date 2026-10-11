<div align="center">

# ⚒️ TaskForge

### Gerenciador de tarefas em Python com PostgreSQL

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-openSUSE-73BA25?style=for-the-badge&logo=opensuse&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.1-8A2BE2?style=for-the-badge)
![Status](https://img.shields.io/badge/v1.5-Em_Desenvolvimento-F59E0B?style=for-the-badge)

**Organize tarefas, defina prioridades e acompanhe o que já foi concluído — diretamente pelo terminal.**

[Sobre](#-sobre-o-projeto) • [Funcionalidades](#-funcionalidades-da-v11) • [Tecnologias](#️-tecnologias) • [Instalação](#-instalação) • [Roadmap](#-roadmap-da-v15)

</div>

---

## 📌 Sobre o projeto

O **TaskForge** é uma aplicação de linha de comando (CLI) desenvolvida em **Python** com persistência de dados no **PostgreSQL**. Seu objetivo é oferecer um gerenciador de tarefas simples e, ao mesmo tempo, servir como projeto prático de aprendizado de Python, SQL e desenvolvimento modular.

A aplicação utiliza consultas SQL para criar, visualizar, editar, concluir e excluir tarefas. Os registros permanecem no banco de dados após o encerramento do programa.

> **Versão atual: 1.1.** A versão **1.5 está em desenvolvimento** e ainda não é considerada uma versão estável ou lançada. Algumas funcionalidades apresentadas no roadmap podem já existir em código de desenvolvimento, mas ainda precisam de testes e integração.

## 🚀 Funcionalidades da v1.1

| Operação | Descrição | SQL |
|:--|:--|:--:|
| 📋 **Listar tarefas** | Exibe ID, título, prioridade e situação | `SELECT` |
| ➕ **Adicionar tarefa** | Cadastra título e prioridade | `INSERT` |
| ✏️ **Editar título** | Altera o nome de uma tarefa existente | `UPDATE` |
| 🎯 **Editar prioridade** | Modifica a prioridade de uma tarefa | `UPDATE` |
| ✅ **Concluir tarefa** | Marca uma tarefa como concluída | `UPDATE` |
| 🗑️ **Remover tarefa** | Exclui uma tarefa existente | `DELETE` |
| 💾 **Persistência** | Armazena as alterações no PostgreSQL | — |

### ⚙️ Recursos da versão atual

- Prioridades padronizadas: **Alta**, **Moderada** e **Baixa**.
- Verificação da existência de tarefas antes das operações de edição.
- Menus e mensagens formatados para uso no terminal.
- Identificadores únicos gerados pelo PostgreSQL.
- Consultas parametrizadas com `%s` por meio do **Psycopg 3**.
- Configuração da senha do banco por variável de ambiente.
- Separação da conexão, das operações e da edição em módulos Python.

> [!IMPORTANT]
> As operações por **título** ainda podem afetar vários registros quando existem títulos iguais. A migração dessas operações para **ID** e a ampliação das validações fazem parte das melhorias planejadas. A validação de prioridades ocorre na aplicação; ainda não há indicação de uma restrição equivalente no banco.

---

## 🛠️ Tecnologias

| Tecnologia | Papel no projeto |
|:--|:--|
| **Python 3.13** | Regras de negócio e interface de terminal |
| **PostgreSQL 18** | Armazenamento relacional das tarefas |
| **Psycopg 3** | Conexão e execução de SQL a partir do Python |
| **python-dotenv** | Carregamento das variáveis de ambiente |
| **SQL** | `SELECT`, `INSERT`, `UPDATE`, `DELETE` e consultas de contagem |
| **openSUSE Linux** | Ambiente de desenvolvimento |
| **Git e GitHub** | Versionamento e publicação |
| **VS Code** | Desenvolvimento e edição do código |

---

## 📂 Estrutura do projeto

Estrutura de referência dos módulos trabalhados no projeto:

```text
TaskForge/
├── menu.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env                  # Local: não enviar ao GitHub
├── database/
│   └── connection.py
└── task/
    ├── task_service.py   # Cadastro, listagem, conclusão e exclusão
    ├── editar.py         # Edição de título e prioridade (v1.1)
    └── tarefa.py         # Representação da tarefa, se separada em módulo
```

Os nomes e a distribuição dos arquivos podem variar conforme os módulos forem reorganizados. O código de **estatísticas da v1.5** está em construção e não é apresentado como recurso lançado.

---

## 🗄️ Banco de dados

A base utiliza uma tabela `tarefas`. A estrutura fundamental da **v1.1** é:

```sql
CREATE TABLE tarefas (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    prioridade VARCHAR(20) NOT NULL,
    concluida BOOLEAN DEFAULT FALSE
);
```

| Coluna | Tipo | Descrição |
|:--|:--|:--|
| `id` | `INTEGER` | Identificador único da tarefa |
| `titulo` | `VARCHAR(150)` | Nome da tarefa |
| `prioridade` | `VARCHAR(20)` | Alta, Moderada ou Baixa, validada no Python |
| `concluida` | `BOOLEAN` | `FALSE` = pendente; `TRUE` = concluída |

**Mudança em desenvolvimento para a v1.5:** adicionar uma coluna opcional de prazo:

```sql
ALTER TABLE tarefas
ADD COLUMN vencimento DATE;
```

> [!NOTE]
> A coluna `vencimento` já faz parte dos estudos e do desenvolvimento da v1.5, mas **não é requisito da versão 1.1**. Execute a migração somente quando quiser testar o código de desenvolvimento que utiliza vencimentos. Se a coluna já existir, não execute o comando novamente.

---

## 🖥️ Prévia do terminal

### 📋 Listar tarefas

```text
========================================
          TASKFORGE v1.1
========================================
             SUAS TAREFAS
========================================
 ID:         1
 Título:     Estudar Python
 Prioridade: Alta
 Situação:   Pendente
----------------------------------------
 ID:         2
 Título:     Revisar SQL
 Prioridade: Moderada
 Situação:   Concluída
========================================
```

### ➕ Adicionar tarefa

```text
========================================
          TASKFORGE v1.1
========================================
           ADICIONAR TAREFA
========================================
 Título da tarefa: Estudar PostgreSQL

         PRIORIDADES DISPONÍVEIS
----------------------------------------
 [1] Alta
 [2] Moderada
 [3] Baixa
----------------------------------------
 Digite a prioridade: Alta

========================================
           TAREFA ADICIONADA!
========================================
 Título:     Estudar PostgreSQL
 Prioridade: Alta
 Situação:   Pendente
========================================
```

### ✏️ Editar tarefa

```text
========================================
          TASKFORGE v1.1
========================================
             EDITAR TAREFA
========================================
 Qual tarefa deseja editar? Estudar Python

 [1] Editar título
 [2] Editar prioridade

 Escolha uma opção: 1
 Digite o novo título: Estudar Python e SQL

========================================
           TAREFA ATUALIZADA!
========================================
 Título anterior: Estudar Python
 Novo título:     Estudar Python e SQL
========================================
```

*Exemplos ilustrativos da interface CLI; a saída exata pode variar entre os módulos.*

---

## 📥 Instalação

### 1. Pré-requisitos

- Python 3 instalado.
- PostgreSQL instalado e em execução.
- Git para clonar o repositório.

### 2. Clonar o repositório

```bash
git clone https://github.com/Mutus142/TaskForge.git
cd TaskForge
```

### 3. Criar o ambiente virtual

No Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
python -m pip install "psycopg[binary]" python-dotenv
```

Se o `requirements.txt` estiver atualizado com as dependências do projeto, também é possível usar `python -m pip install -r requirements.txt`.

### 5. Preparar o PostgreSQL

Crie o banco de dados e execute a definição da tabela apresentada em [Banco de dados](#️-banco-de-dados). A configuração de conexão utilizada no projeto é baseada em:

```python
host="localhost"
port=5432
dbname="TaskForge"
user="taskforge_user"
```

Crie ou configure esse usuário com as permissões adequadas. No PostgreSQL, nomes criados entre aspas preservam maiúsculas/minúsculas — isso vale para `"TaskForge"`.

### 6. Configurar a senha

Crie um arquivo `.env` na raiz do projeto:

```env
TASKFORGE_DB_PASSWORD=sua_senha_aqui
```

> [!CAUTION]
> Nunca envie o `.env` com credenciais reais ao GitHub. Confirme que ele consta no `.gitignore`.

### 7. Executar a aplicação

A entrada do projeto é o menu em `menu.py`:

```bash
python menu.py
```

Caso esteja testando funções isoladamente, uma operação também pode ser executada pelo módulo correspondente, por exemplo:

```bash
python -c "from task.task_service import ver_task; ver_task()"
```

> [!NOTE]
> A execução depende de a configuração do PostgreSQL estar correta e de o menu importar as funções dos módulos existentes. Os exemplos representam a organização desenvolvida até aqui.

---

## 📝 Histórico de versões

### ✅ v1.0 — Base do TaskForge

- Estrutura inicial em Python.
- Conexão e persistência com PostgreSQL.
- Cadastro, listagem, conclusão e remoção de tarefas.
- Identificador automático, prioridade e situação de conclusão.
- SQL parametrizado e configuração de credenciais fora do código.

### ✅ v1.1 — Edição e melhorias de usabilidade **(versão atual)**

- Criação do módulo `task/editar.py`.
- Edição de títulos de tarefas.
- Edição de prioridades.
- Opções de prioridade limitadas a **Alta**, **Moderada** e **Baixa** no fluxo de cadastro e edição.
- Verificações de existência de tarefas durante a edição.
- Revisão e padronização visual dos menus e mensagens.
- Melhor organização das operações em funções e módulos.

### 🚧 v1.5 — Productivity Update **(em desenvolvimento)**

- Inclusão de data de vencimento nas tarefas.
- Conversão e comparação de datas com `datetime`.
- Consulta de quantidades de tarefas cadastradas, concluídas e pendentes.
- Menu específico de estatísticas e resumo geral.
- Evolução da listagem para considerar prazos.

*Esses recursos estão sendo implementados e revisados; não representam uma versão 1.5 já publicada.*

---

## 🔮 Roadmap da v1.5

- [x] Iniciar cadastro de vencimentos com `datetime` e PostgreSQL.
- [x] Desenvolver as primeiras consultas de estatísticas (`COUNT`).
- [x] Criar a estrutura inicial do menu de estatísticas.
- [ ] Validar datas inválidas e títulos vazios de forma consistente.
- [ ] Identificar automaticamente tarefas atrasadas, com vencimento hoje ou dentro do prazo.
- [ ] Adicionar filtros de listagem por situação, prioridade e vencimento.
- [ ] Implementar taxa de conclusão das tarefas.
- [ ] Migrar operações sensíveis ao título para identificação por ID.
- [ ] Consolidar e testar a integração entre menu, edição, vencimentos e estatísticas.
- [ ] Escrever testes automatizados e revisar mensagens de erro.
- [ ] Publicar e marcar a versão **v1.5** após a validação final.

**Ideias para a v2.0:** API REST com FastAPI e, futuramente, uma interface web.

---

## 👨‍💻 Desenvolvedor

<div align="center">

### Mateus — [Mutus142](https://github.com/Mutus142)

Projeto criado para aprofundar conhecimentos em **Python, SQL, PostgreSQL e desenvolvimento de aplicações com banco de dados**.

[![GitHub](https://img.shields.io/badge/GitHub-Mutus142-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mutus142)

**⭐ Se o projeto foi útil ou interessante, considere deixar uma estrela no repositório!**

</div>
