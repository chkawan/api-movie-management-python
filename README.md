<<<<<<< HEAD
# 🎬 Flix API - Sistema de Gerenciamento de Filmes

## 📄 Descrição

API REST desenvolvida com Django para gerenciamento de filmes, incluindo entidades como gêneros, atores, filmes e avaliações.

A aplicação permite operações completas de CRUD e modela relacionamentos entre os dados, como filmes associados a gêneros e atores, além de avaliações vinculadas aos filmes.

---

## 🚀 Funcionalidades

* CRUD completo de:

  * Gêneros (Genres)
  * Atores (Actors)
  * Filmes (Movies)
  * Avaliações (Reviews)
* Relacionamentos entre entidades:

  * Filme → Gênero
  * Filme → Atores
  * Review → Filme
* Estrutura de endpoints versionada (`/api/v1/`)
* Integração com Postman (coleção pronta)

---

## 🧠 Como funciona

A API segue o padrão REST e organiza os recursos em endpoints separados:

### 📂 Recursos disponíveis

* `/api/v1/genres/` → Gerenciamento de gêneros
* `/api/v1/actors/` → Gerenciamento de atores
* `/api/v1/movies/` → Gerenciamento de filmes
* `/api/v1/reviews/` → Gerenciamento de avaliações

Cada recurso permite:

* `GET` → Listar e detalhar
* `POST` → Criar
* `PUT` → Atualizar
* `DELETE` → Remover

---

## 🛠️ Tecnologias utilizadas

* Python
* Django
* Django REST Framework
* SQLite (padrão)
* Postman (testes de API)

---

## 📦 Estrutura do projeto (resumo)

```bash
.
├── api/
│   ├── genres/
│   ├── actors/
│   ├── movies/
│   ├── reviews/
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## ⚙️ Pré-requisitos

* Python 3.8+
* Pip
* Virtualenv (opcional)

---

## 🖥️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

---

### 2. Criar ambiente virtual

```bash
python -m venv env
```

Ativar:

* Windows:

```bash
env\Scripts\activate
```

* Linux/Mac:

```bash
source env/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Rodar migrações

```bash
python manage.py migrate
```

---

### 5. Iniciar servidor

```bash
python manage.py runserver
```

---

### 6. Acessar API

```bash
http://127.0.0.1:8000/api/v1/
```

---

## 📬 Testando com Postman

A coleção inclui endpoints para:

* Gêneros
* Atores
* Filmes
* Reviews

### 🔹 Exemplo de criação de filme

```json
{
  "title": "Filme Exemplo",
  "genre": 1,
  "release_date": "2024-04-04",
  "actors": [1],
  "resume": "Resumo do filme."
}
```

---

## 🔗 Relacionamentos

* Um filme possui:

  * 1 gênero
  * Vários atores
* Uma review está associada a:

  * 1 filme

---

## 🔐 Observações

* A API utiliza estrutura versionada (`v1`)
* IDs são utilizados para relacionamentos entre entidades
* Pode ser facilmente expandida com autenticação (JWT)

---

## ⚡ Possíveis melhorias

* Autenticação com JWT
* Paginação e filtros
* Upload de imagens (posters de filmes)
* Documentação automática (Swagger/OpenAPI)
* Permissões por usuário
* Deploy em produção (Docker + cloud)

---

## 📄 Licença

Projeto de uso educacional e livre para adaptações.

---

## 👨‍💻 Autor

Desenvolvido por **Christopher Kawan**
=======
# 🎬 Flix API - Sistema de Gerenciamento de Filmes

## 📄 Descrição

API REST desenvolvida com Django para gerenciamento de filmes, incluindo entidades como gêneros, atores, filmes e avaliações.

A aplicação permite operações completas de CRUD e modela relacionamentos entre os dados, como filmes associados a gêneros e atores, além de avaliações vinculadas aos filmes.

---

## 🚀 Funcionalidades

* CRUD completo de:

  * Gêneros (Genres)
  * Atores (Actors)
  * Filmes (Movies)
  * Avaliações (Reviews)
* Relacionamentos entre entidades:

  * Filme → Gênero
  * Filme → Atores
  * Review → Filme
* Estrutura de endpoints versionada (`/api/v1/`)
* Integração com Postman (coleção pronta)

---

## 🧠 Como funciona

A API segue o padrão REST e organiza os recursos em endpoints separados:

### 📂 Recursos disponíveis

* `/api/v1/genres/` → Gerenciamento de gêneros
* `/api/v1/actors/` → Gerenciamento de atores
* `/api/v1/movies/` → Gerenciamento de filmes
* `/api/v1/reviews/` → Gerenciamento de avaliações

Cada recurso permite:

* `GET` → Listar e detalhar
* `POST` → Criar
* `PUT` → Atualizar
* `DELETE` → Remover

---

## 🛠️ Tecnologias utilizadas

* Python
* Django
* Django REST Framework
* SQLite (padrão)
* Postman (testes de API)

---

## 📦 Estrutura do projeto (resumo)

```bash
.
├── api/
│   ├── genres/
│   ├── actors/
│   ├── movies/
│   ├── reviews/
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## ⚙️ Pré-requisitos

* Python 3.8+
* Pip
* Virtualenv (opcional)

---

## 🖥️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

---

### 2. Criar ambiente virtual

```bash
python -m venv env
```

Ativar:

* Windows:

```bash
env\Scripts\activate
```

* Linux/Mac:

```bash
source env/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Rodar migrações

```bash
python manage.py migrate
```

---

### 5. Iniciar servidor

```bash
python manage.py runserver
```

---

### 6. Acessar API

```bash
http://127.0.0.1:8000/api/v1/
```

---

## 📬 Testando com Postman

A coleção inclui endpoints para:

* Gêneros
* Atores
* Filmes
* Reviews

### 🔹 Exemplo de criação de filme

```json
{
  "title": "Filme Exemplo",
  "genre": 1,
  "release_date": "2024-04-04",
  "actors": [1],
  "resume": "Resumo do filme."
}
```

---

## 🔗 Relacionamentos

* Um filme possui:

  * 1 gênero
  * Vários atores
* Uma review está associada a:

  * 1 filme

---

## 🔐 Observações

* A API utiliza estrutura versionada (`v1`)
* IDs são utilizados para relacionamentos entre entidades
* Pode ser facilmente expandida com autenticação (JWT)

---

## ⚡ Possíveis melhorias

* Autenticação com JWT
* Paginação e filtros
* Upload de imagens (posters de filmes)
* Documentação automática (Swagger/OpenAPI)
* Permissões por usuário
* Deploy em produção (Docker + cloud)

---

## 📄 Licença

Projeto de uso educacional e livre para adaptações.

---

## 👨‍💻 Autor

Desenvolvido por **Christopher Kawan**
>>>>>>> 50e4405 (First commit - API Movie Management)
