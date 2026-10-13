<div align="center">

# ⚒️ TaskForge

### Gerenciador de tarefas CLI com Python e PostgreSQL

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-openSUSE-73BA25?style=for-the-badge&logo=opensuse&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.5-8A2BE2?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Lan%C3%A7amento_v1.5-22C55E?style=for-the-badge)

**Organize tarefas, acompanhe vencimentos e consulte estatísticas — com contas individuais e armazenamento persistente.**

[Sobre](#-sobre-o-projeto) • [Funcionalidades](#-funcionalidades) • [Instalação](#-instalação-e-execução) • [Versões](#-histórico-de-versões) • [Limitações](#-limitações-conhecidas)

</div>

---

## 📌 Sobre o projeto

O **TaskForge** é um gerenciador de tarefas executado pelo terminal, desenvolvido em **Python** e integrado ao **PostgreSQL** por meio do Psycopg 3.

O projeto foi criado para praticar lógica de programação, organização modular, SQL, manipulação de datas e integração entre aplicações e bancos de dados relacionais.

A **versão 1.5** expande o CRUD original com **cadastro e login de usuários, tarefas vinculadas à conta autenticada, prazos e estatísticas**. Os dados continuam armazenados após o encerramento da aplicação.

> [!NOTE]
> Projeto educacional, em evolução. A v1.5 é a versão de lançamento atual; melhorias de validação e segurança permanecem planejadas.

## 🚀 Funcionalidades

| Recurso | Descrição | Principais recursos técnicos |
|:--|:--|:--|
| 👤 **Cadastro de usuários** | Criação de contas com nome, username e senha de teste | `INSERT`, `UNIQUE` |
| 🔑 **Login** | Identificação da conta e acesso ao menu | `SELECT`, `usuario_id` |
| 📋 **Listagem de tarefas** | Mostra somente as tarefas da conta autenticada | `SELECT`, `WHERE` |
| ➕ **Cadastro de tarefas** | Adiciona título, prioridade e vencimento | `INSERT`, `DATE` |
| ✏️ **Edição** | Altera título ou prioridade | `UPDATE` |
| ✅ **Conclusão** | Marca tarefas como concluídas | `UPDATE` |
| 🗑️ **Exclusão** | Remove tarefas existentes | `DELETE` |
| 📊 **Estatísticas** | Conta cadastradas, concluídas, pendentes e atrasadas | `COUNT()`, `CURRENT_DATE` |
| 💾 **Persistência** | Armazena usuários e tarefas no PostgreSQL | Psycopg 3 |

### ⚙️ Recursos adicionais

- Prioridades disponíveis: **Alta**, **Moderada** e **Baixa**.
- Datas de vencimento informadas no formato **DD/MM/AAAA**.
- Avisos para datas passadas, vencimento no dia e datas futuras.
- Estatísticas gerais e individuais, filtradas pelo usuário autenticado.
- Menus e mensagens padronizados no terminal.
- Consultas SQL parametrizadas com `%s`.
- Organização do código em módulos de usuários, tarefas e conexão.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|:--|:--|
| **Python 3.13** | Lógica, interface CLI e manipulação de datas |
| **PostgreSQL** | Banco de dados relacional |
| **Psycopg 3** | Comunicação Python–PostgreSQL |
| **python-dotenv** | Leitura de configurações em `.env` |
| **datetime** | Validação e formatação de datas |
| **SQL** | CRUD, filtros e estatísticas |
| **Git / GitHub** | Versionamento e documentação |
| **openSUSE / VS Code** | Ambiente de desenvolvimento |

## 📂 Estrutura do projeto

```text
TaskForge/
├── main.py                # Entrada principal da aplicação
├── menu.py                # Menu após autenticação
├── README.md
├── requirements.txt
├── .gitignore
├── .env                   # Configurações locais; não versionar
├── database/
│   └── connection.py      # Conexão com PostgreSQL
├── user/
│   ├── cadastro.py        # Cadastro de usuários
│   └── login.py           # Login e fluxo de acesso
└── task/
    ├── task_service.py   # Listar, adicionar, remover e concluir
    ├── editar.py         # Editar título e prioridade
    └── estatistica.py    # Indicadores e contagens
```

*Estrutura dos arquivos principais trabalhados no projeto; outros arquivos auxiliares podem existir no repositório.*

## 🗄️ Banco de dados

O relacionamento é de **um usuário para muitas tarefas (1:N)**, por meio da chave estrangeira `tarefas.usuario_id`.

### Exemplo de esquema para uma instalação nova

```sql
CREATE TABLE usuarios (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tarefas (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    prioridade VARCHAR(20) NOT NULL,
    concluida BOOLEAN DEFAULT FALSE,
    vencimento DATE,
    usuario_id INTEGER REFERENCES usuarios(id)
);
```

> [!IMPORTANT]
> Esse SQL é um **exemplo de criação para banco vazio**. Caso já possua a base das versões anteriores, **não recrie as tabelas**: preserve seus dados e utilize migrações como `ALTER TABLE` para adicionar as colunas necessárias. Tarefas antigas com `usuario_id = NULL` não aparecem nas consultas filtradas por conta até serem associadas a um usuário.

## 🖥️ Prévia do terminal

### Login

```text
========================================
          TASKFORGE v1.5
========================================
           SISTEMA DE LOGIN
========================================

 Digite seu usuário: mutus
 Digite sua senha: ********

========================================
          LOGIN REALIZADO!
========================================
```

### Menu principal

```text
========================================
              TASKFORGE
               v1.5
========================================
 [1] Ver tarefas
 [2] Adicionar tarefa
 [3] Remover tarefa
 [4] Editar tarefa
 [5] Concluir tarefa
 [6] Estatísticas
 [0] Sair
----------------------------------------
```

### Tarefas

```text
========================================
          TASKFORGE v1.5
========================================
             SUAS TAREFAS
========================================
 ID:         1
 Título:     Estudar PostgreSQL
 Prioridade: Alta
 Vencimento: 20/10/2026
 Situação:   Pendente
----------------------------------------
```

### Estatísticas

```text
========================================
          TASKFORGE v1.5
========================================
         ESTATÍSTICAS GERAIS
========================================
 Tarefas cadastradas: 10
 Tarefas concluídas:  6
 Tarefas pendentes:   4
========================================
```

*As telas são ilustrativas; os valores dependem dos dados de cada usuário.*

## 📥 Instalação e execução

### 1. Pré-requisitos

- Python 3.13 (ou versão compatível).
- PostgreSQL instalado e em execução.
- Git.

### 2. Clonar o repositório

```bash
git clone https://github.com/Mutus142/TaskForge.git
cd TaskForge
```

### 3. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

### 4. Instalar dependências

```bash
./.venv/bin/python -m pip install -r requirements.txt
```

Caso o arquivo de dependências ainda não esteja atualizado, as principais bibliotecas externas utilizadas são `psycopg[binary]` e `python-dotenv`.

### 5. Configurar o banco de dados

Crie o banco PostgreSQL, prepare as tabelas descritas acima e confira as configurações de conexão em `database/connection.py`.

Configure a senha em um arquivo `.env` na raiz do projeto, conforme a variável esperada pelo módulo de conexão. Na configuração trabalhada durante o desenvolvimento:

```env
TASKFORGE_DB_PASSWORD=sua_senha_de_teste
```

> [!CAUTION]
> Nunca publique seu `.env` nem credenciais reais no GitHub. Confirme que `.env` e `.venv/` estão no `.gitignore`.

### 6. Iniciar o TaskForge

No Linux, a partir da raiz do projeto:

```bash
./.venv/bin/python main.py
```

O sistema inicia pela tela de login e libera o menu de tarefas após a autenticação.

## 📝 Histórico de versões

### ✅ v1.5 — Usuários, vencimentos e estatísticas

- Cadastro e login de usuários.
- Tarefas vinculadas por `usuario_id`.
- Listagem, edição, conclusão e remoção restritas à conta autenticada.
- Datas de vencimento armazenadas no PostgreSQL.
- Estatísticas de tarefas cadastradas, concluídas, pendentes e atrasadas.
- Interface CLI padronizada e fluxo centralizado em `main.py`.

### ✅ v1.1 — Edição e validações

- Edição de título e prioridade.
- Padronização de prioridades (Alta, Moderada e Baixa).
- Melhorias de organização dos arquivos e mensagens do terminal.

### ✅ v1.0 — Base do projeto

- Conexão Python + PostgreSQL.
- Operações CRUD e persistência.
- Consultas SQL parametrizadas.
- Organização inicial da aplicação.

## ⚠️ Limitações conhecidas

- **Senhas de teste em texto puro:** na implementação educacional atual, o campo `senha_hash` não armazena necessariamente um hash. **Não use senhas reais e não disponibilize essa autenticação para uso público.** Uma versão destinada a usuários reais precisará de hash de senhas e reforços de segurança.
- **Operações por título:** quando um mesmo usuário tem tarefas com títulos iguais, editar, concluir ou excluir pode afetar mais de um registro. A migração para identificação por **ID** está planejada.
- **Validações e navegação:** o projeto ainda poderá receber melhorias no tratamento de exceções, tentativas repetidas de login e logout.
- **Tarefas legadas:** registros anteriores à implementação das contas podem precisar de associação manual ao usuário correto.

## 🔮 Próximas melhorias

- [ ] Atualizar operações de edição, conclusão e remoção para usar ID.
- [ ] Substituir tentativas recursivas de login por um fluxo iterativo.
- [ ] Implementar logout explícito e retorno à tela inicial.
- [ ] Ampliar os testes automatizados e o tratamento de erros.
- [ ] Melhorar a autenticação antes de qualquer uso fora de um ambiente de estudo.
- [ ] Adicionar filtros avançados por prioridade e vencimento.

---

## 👨‍💻 Desenvolvedor

<div align="center">

### Mateus — Mutus142

Projeto desenvolvido para aprofundar conhecimentos em **Python, SQL, PostgreSQL e desenvolvimento de software**.

[![GitHub](https://img.shields.io/badge/GitHub-Mutus142-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mutus142)

**⭐ Se gostou do projeto, considere deixar uma estrela no repositório!**

</div>
