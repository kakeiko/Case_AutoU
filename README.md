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

### 5. Rodas as migrações

```bash
python manage.py migrate
```

### 6. Iniciar o servidor

```bash
python manage.py runserver
```
