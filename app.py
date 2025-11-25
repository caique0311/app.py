from flask import Flask, request, jsonify
import os
import requests
import traceback
from dotenv import load_dotenv

# caminho ABSOLUTO do .env
ENV_PATH = r"C:\Users\Tamiris Rodrigues\Downloads\chat.ia\.env"
load_dotenv(ENV_PATH)

# Busque a variável pelo NOME que você deu a ela no arquivo .env
api_key = os.getenv("AIzaSyCLxMT--3X6EAfMKCb0mGtH9ZLsJGEq3JI")

# --- DEBUGGING: VAMOS VER O QUE FOI LIDO ---
print(f"DEBUG: O script está tentando carregar o arquivo em: {ENV_PATH}")
print(f"DEBUG: Valor lido para GEMINI_API_KEY: {api_key if api_key else 'NÃO ENCONTRADO/VAZIO'}")
# ------------------------------------------

if not api_key:
    # Se a chave AINDA não for encontrada, o erro agora faz mais sentido
    raise RuntimeError(f"❌ GEMINI_API_KEY não encontrada!\nVerifique o arquivo .env em: {ENV_PATH}")

app = Flask(__name__)

GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

@app.route("/")
def home():
    return "API está online. Envie POST para /ask"

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        pergunta = data.get("question", "")

        if not pergunta:
            return jsonify({"answer": "Nenhuma pergunta fornecida."}), 400

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": pergunta}
                    ]
                }
            ]
        }

        response = requests.post(GEMINI_URL, json=payload)
        
        # Verifica se a requisição à API Gemini foi bem-sucedida
        if response.status_code != 200:
            print(f"Erro na API Gemini: {response.status_code}")
            print(response.json())
            return jsonify({"answer": f"Erro ao contatar a API Gemini: {response.text}"}), response.status_code

        result = response.json()

        print("\n===== RESPOSTA COMPLETA DO GEMINI =====")
        print(result)
        print("=======================================\n")

        # Tratamento de erro mais robusto para a resposta
        if "candidates" not in result or not result["candidates"]:
            error_message = result.get("error", {}).get("message", "Resposta inesperada da API.")
            print(f"Erro na resposta do Gemini: {error_message}")
            return jsonify({"answer": f"Erro na resposta do Gemini: {error_message}"}), 500

        resposta = result["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"answer": resposta})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"answer": f"Erro interno no servidor: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(port=8080)