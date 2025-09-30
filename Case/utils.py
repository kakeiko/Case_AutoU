import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("API_KEY"))

def bot_classifica(email):
    df = pd.read_csv("C:\\Users\\Pichau\\Documents\\workspace\\pessoal\\python\\CaseAutoU\\Case\\emails.csv")
    df = df.dropna()
    X_train, X_test, y_train, y_test = train_test_split(df["texto"], df["rotulo"], test_size=0.2)

    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    model = LogisticRegression()
    model.fit(X_train_tfidf, y_train)
    documento_para_prever = [email]

    prova_tfidf = vectorizer.transform(documento_para_prever)

    previsao = model.predict(prova_tfidf)
    return str(previsao[0])

def gerar_resposta(email, produtivo):
    if produtivo:
        prompt = f"""
                    Você é um assistente que redige respostas profissionais em português do Brasil.

                    Tarefa:
                    - Leia atentamente o e-mail abaixo.
                    - Crie uma resposta educada e completa, que:
                    • Confirme o recebimento.
                    • Aborde todos os pontos importantes.
                    • Proponha próximos passos ou esclarecimentos, se necessário.
                    • Use tom profissional, mas cordial.

                    E-mail recebido:
                    "{email}"
                    """
    else:
        prompt = f"""
                    Você é um assistente que responde e-mails em português do Brasil.

                    Tarefa:
                    - Leia o e-mail abaixo.
                    - Gere uma resposta curta, educada e neutra, informando que:
                    • A mensagem não se enquadra no escopo de atendimento, OU
                    • Não há ação necessária no momento.
                    - Mantenha tom respeitoso e objetivo.

                    E-mail recebido:
                    "{email}"

                    Forneça apenas a resposta final, em até 3 frases.
                    """
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"[Erro ao gerar resposta: {e}]"
