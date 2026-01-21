import re
import requests
import unicodedata
import os
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer

load_dotenv()

vectorizer = TfidfVectorizer(
    stop_words="Portugues",
    max_features=20
)

def process_email(email):
    if isinstance(email, list):
        email = " ".join(email)
    STOPWORDS_PT = [
        "a", "o", "e", "de", "do", "da", "dos", "das", "em", "para",
        "por", "com", "que", "na", "no", "nos", "nas", "um", "uma",
        "é", "ser", "foi", "são", "ao", "à", "às", "se", "sua",
        "seu", "seus", "suas", "como", "mais", "mas", "ou", "já",
        "não", "sim", "também", "até", "sobre", "entre", "após",
        "antes", "essa", "esse", "isso", "esta", "este"
    ]
    email_clear = email.lower()
    email_clear = unicodedata.normalize("NFKD", email_clear).encode("ascii", "ignore").decode("utf-8")
    email_clear = re.sub(r"http\S+", "", email_clear)
    email_clear = re.sub(r"[^a-zA-Z0-9\s]", "", email_clear)
    email_clear = re.sub(r"\s+", " ", email_clear)

    vectorizer = TfidfVectorizer(
        stop_words=STOPWORDS_PT,
        max_features=10
    )

    tfidf = vectorizer.fit_transform([email_clear])
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf.toarray()[0]

    keywords = [
        word for word, score in sorted(
            zip(feature_names, scores),
            key=lambda x: x[1],
            reverse=True
        )
        if score > 0
    ]

    dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", email)

    has_link = "http" in email.lower() or "clique aqui" in email.lower()
    return {
        "clean_text": email_clear,
        "keywords": keywords,
        "dates": dates,
        "has_link": has_link,
    }

def response_email(email):
    response = requests.post(
        os.getenv("N8N_LINK"),
        json=email,
        timeout=10
    )
    resposta = response.json()
    resposta = resposta['resultado'].split('/', 1)
    classificao = resposta[0]
    resultado = resposta[1]
    
    return classificao, resultado
