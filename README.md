# Case_AutoU

Automação de leitura e classificação de e-mails e sugestão de resposta com Django + Pandas + scikit-learn + OpenAI API.

---

## 🚀 Tecnologias

- [Python 3.11+](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [N8N](https://n8n.io)
- [Render](https://render.com/) para deploy (O plano gratuito do render entra em modo sleep depois de 15 minutos sem requisição, e demora alguns segundos para voltar pro ar, por favor espere.)

---

## ⚙️ Como rodar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/kakeiko/Case_AutoU.git
cd Case_AutoU
```

### 2. Criar um ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/macOS
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar as variavéis

Criar um arquivo .env na raiz do projeto e adicionar as seguintes informações:

```env
SECRET_KEY = 'django-insecure-aw4gljtyx-l$f)lu6xg8=acos^$fs&@a*@%s1ls9nzzuk)#b_h'
N8N_LINK = '[Seu link do n8n]'
```
### 5. Configurar bancos de dados

Recomendo usar o SQLite para isso substitua a linha 79 até a linha 88 do settings.py, por isso:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 6. Rodas as migrações

```bash
python manage.py migrate
```

### 7. Subir o n8n com Docker (local)

O n8n será usado para automatizar a leitura e classificação de e-mails e se comunicar com a aplicação Django.

#### 7.1. Pré-requisitos

-Docker instalado e em execução

#### 7.2. Baixar a imagem do n8n
```bash
docker pull n8nio/n8n
```

#### 7.3. Rodar o n8n localmente

Execute o comando abaixo para subir o n8n:
```bash
docker run -it --rm ^
  -p 5678:5678 ^
  -v n8n_data:/home/node/.n8n ^
  --name n8n ^
  n8nio/n8n
```

#### 7.4. Acessar o n8n

Abra o navegador e acesse:

http://localhost:5678


Na primeira vez, o n8n pedirá para criar um usuário (e-mail e senha).

#### 7.5. Configurar o link do n8n no projeto Django

No arquivo .env, configure o link do n8n:
```env
N8N_LINK=http://localhost:5678
```

Se o Django estiver rodando localmente, essa configuração já é suficiente.

### 8. Iniciar o servidor

```bash
python manage.py runserver
```



