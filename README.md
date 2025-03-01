# LCCV - Prova Back-End 🔧

Projeto Django com PostgreSQL.

## 📌 Pré-requisitos
- Python 3.8+
- PostgreSQL 16
- Git

---

## 🐘 Instalação do PostgreSQL

### Windows
1. Baixe o instalador em [postgresql.org/download/windows](https://www.postgresql.org/download/windows/)
2. Siga o assistente de instalação (marque a opção "Add to PATH")
3. Mantenha a porta padrão (5432) e senha do usuário `postgres`

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

---

## 🛠️ Configurar Banco de Dados

```bash
sudo -u postgres psql
```
```sql
CREATE DATABASE lccv;
CREATE USER lccvUsr WITH PASSWORD '1010';
ALTER ROLE lccvUsr SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE lccv TO lccvUsr;
\q
```

### Configuração no Django

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lccv',       # Nome do banco
        'USER': 'lccvUsr',    # Seu usuário
        'PASSWORD': '1010',   # Sua senha
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🚀 Instalação do Projeto

```bash
# Clonar repositório
git clone https://github.com/gabrielsantz/projLCCV.git
cd projLCCV/django

# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Instalar dependências
pip install -r requirements.txt

# Aplicar migrações
cd lccv
python manage.py makemigrations
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser
# Preencha os dados solicitados

# Iniciar o servidor
python manage.py runserver
```

---

## Endpoints Disponíveis

### Projetos
- **GET** `/projetos/listar/` - Lista todos os projetos
- **POST** `/projetos/cadastrar/` - Cadastra novo projeto

### Colaboradores
- **GET** `/colaboradores/listar/` - Lista colaboradores
- **POST** `/colaboradores/cadastrar/` - Cadastra novo colaborador

---

## Painel Admin

Acesse [http://localhost:8000/admin](http://localhost:8000/admin) para:
- Gerenciar modelos
- Verificar dados
- Criar/Editar registros

