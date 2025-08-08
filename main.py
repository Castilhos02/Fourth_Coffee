import pandas as pd
from textblob import TextBlob

# Carregar feedbacks
with open("dados/feedbacks.txt", "r", encoding="utf-8") as f:
    feedbacks = f.readlines()

# Analisar feedbacks
def analisar_feedback(texto):
    blob = TextBlob(texto)
    sentimento = blob.sentiment.polarity
    return {
        "texto": texto.strip(),
        "frases_chave": ", ".join(blob.noun_phrases),
        "sentimento": "Positivo" if sentimento > 0 else "Negativo" if sentimento < 0 else "Neutro"
    }

dados = [analisar_feedback(fb) for fb in feedbacks]
df = pd.DataFrame(dados)
df.to_csv("informacoes/feedbacks_enriquecidos.csv", index=False)

# Busca por palavra-chave
def buscar_feedbacks(palavra):
    resultados = df[df['texto'].str.contains(palavra, case=False)]
    return resultados[['texto', 'sentimento']]

# Exemplo de busca
resultados = buscar_feedbacks("café")
resultados.to_string("conhecimento/busca_exemplo_cafe.txt")

print("✅ Análise concluída. Resultados salvos.")