from huggingface_hub import InferenceClient

# Substitueix per la teva clau d'API
client = InferenceClient(
    provider="together",
    api_key="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",
)

# Exemple de log
log = '127.0.0.1 - - [05/May/2025:10:21:12 +0000] "GET /index.html HTTP/1.1" 200 2326'

# Instrucció per al model
prompt = f"""
### Instrucció:
Analitza el següent log d'un servidor Apache i explica detalladament què significa cada part. També indica si hi ha alguna cosa sospitosa.

Log:
{log}

### Resposta:
"""

# Enviem la petició
completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
)

# Imprimim la resposta
print(completion.choices[0].message.content)
