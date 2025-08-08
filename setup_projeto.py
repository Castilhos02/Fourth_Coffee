import os
import pandas as pd
from textblob import TextBlob

# Estrutura de pastas
pastas = ["dados", "informacoes", "conhecimento", "prints"]
for pasta in pastas:
    os.makedirs(pasta, exist_ok=True)

# Dados fictícios
feedbacks = [
    "Adorei o atendimento, mas o café estava frio.",
    "Ambiente agradável, mas o pedido demorou.",
    "O café estava excelente, mas achei o preço alto.",
    "Funcionários simpáticos e serviço rápido.",
    "Não gostei do ambiente, muito barulhento."
]

# Salvar feedbacks brutos
with open("dados/feedbacks.txt", "w", encoding="utf-8") as f:
    for fb in feedbacks:
        f.write(fb + "\n")

# Enriquecer dados
def analisar_feedback(texto):
    blob = TextBlob(texto)
    sentimento = blob.sentiment.polarity
    return {
        "texto": texto,
        "frases_chave": ", ".join(blob.noun_phrases),
        "sentimento": "Positivo" if sentimento > 0 else "Negativo" if sentimento < 0 else "Neutro"
    }

dados = [analisar_feedback(fb) for fb in feedbacks]
df = pd.DataFrame(dados)
df.to_csv("informacoes/feedbacks_enriquecidos.csv", index=False)

# Simular busca
palavra = "café"
resultados = df[df['texto'].str.contains(palavra, case=False)]
with open("conhecimento/busca_exemplo_cafe.txt", "w", encoding="utf-8") as f:
    f.write(f"Resultados da busca por '{palavra}':\n\n")
    for _, row in resultados.iterrows():
        f.write(f"Texto: {row['texto']}\nSentimento: {row['sentimento']}\n\n")

print("✅ Projeto estruturado com sucesso!")