# 📘 Explicació dels Logs d'Apache amb Mistral-7B

Aquest repositori conté un script en Python que utilitza el model Mistral-7B de Hugging Face per analitzar i explicar els logs d'Apache, identificant errors i oferint informació detallada.

---

## 🗂️ **Contingut del Repositori**
1. **[`script.py`](/home/adam/Escritorio/tests/mistral.py)**  
   Conté el codi Python per a consumir l'API de Mistral-7B i analitzar els logs d'Apache.
   
2. **`/venv`**  
   Entorn virtual necessari per executar el model, assegurant l'ús d'una versió específica de Python sense afectar altres aplicacions.

---

## 🔍 **Definicions de Paraules Clau**
- **RAG (Retrieval-Augmented Generation):** Mètode que permet recuperar informació rellevant per millorar les respostes generades pel model.  
   *Exemple:* Si un log d'Apache mostra un error 404, el model pot recuperar informació sobre les possibles causes i oferir una explicació detallada.

- **FINE-TUNED:** Model que ha estat entrenat específicament per a tasques com l'anàlisi de logs i detecció d'errors concrets en servidors.

- **TEMPERATURE:** Paràmetre que controla l'aleatorietat de les respostes del model. Valors alts = més creativitat; valors baixos = més precisió.  
   *Exemple:* Amb un valor de temperatura alt, el model podria suggerir múltiples explicacions per a un error; amb un valor baix, aniria directament a la causa més probable.

---

## ⚙️ **Funcionament**
1. Primer, cal consumir l'API de Hugging Face del model **Mistral-7B**, que pots trobar en el següent enllaç:  
   [🔗 Mistral-7B Instruct v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3?inference_api=true&language=python&inference_provider=hf-inference)

2. Perquè l'API funcioni, és necessari crear un **token personal** al teu perfil de Hugging Face. El trobaràs dins de la configuració del teu compte.

3. Un cop generat el token i configurada l'API amb el model seleccionat, ja pots executar el script per analitzar els logs.

---

## ⚖️ **Diferències entre Consumir l'API i Descarregar el Model**
| Mètode          | Recursos Necessaris                                           | Avantatges                               |
|------------------|--------------------------------------------------------------|-----------------------------------------|
| **Descarregar** | - RAM requerida: **32 GB** (sense quantització)              | + Independència de servidors externs    |
|                 | - GPU recomanada: **≥16 GB VRAM** (NVIDIA A100, RTX 3090...) | + Accés immediat un cop carregat        |
|                 | - Amb quantització (bitsandbytes 4-bit): mínim **8-12 GB**   |                                         |
|                 | - Temps d'inferència: entre **10 segons i 2 minuts**         |                                         |
| **Consumir API** | - Només l'script Python                                     | + Ús mínim de CPU i memòria             |
|                 | - Execució en servidors de Hugging Face                      | + Sense necessitat de grans recursos    |

🔹 **Conclusió:**  
Si no disposes d'una màquina amb altes prestacions, l'opció més viable és consumir l'API. Això et permet aprofitar el model sense saturar els recursos locals.

---

## 🚀 **Com Executar**
```bash
# Clonar el repositori
git clone https://github.com/llmopt/asix1-practica1-adamoughriss

# Accedir al directori
cd asix1-practica1-adamoughriss

# Activar l'entorn virtual
source venv/bin/activate

# Executar el script
python script.py
```

---

## ✍️ **Autor**  
Projecte desenvolupat per Adam Oughriss.

---
