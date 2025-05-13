from huggingface_hub import InferenceClient

# Substitueix per la teva clau d'API
client = InferenceClient(
    provider="hf-inference",
    api_key="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",
)

# 🔹 Sol·licitem l'input del log a l'usuari
log = input("Introdueix el log d'Apache que vols analitzar: ")

# 🔹 Optimització del prompt per reduir l'ús de tokens
prompt = f"Explica detalladament el següent log d'Apache i detecta possibles problemes:\n\n{log}\n"

# 🔹 Enviem la petició al model
completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    messages=[{"role": "user", "content": prompt}],
)

# 🔹 Imprimim la resposta
print("\n💡 Explicació del log:\n")
print(completion.choices[0].message.content)
