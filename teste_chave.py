import os
from google import genai
from google.genai.errors import APIError

# Coloque a sua chave de API aqui
CHAVE = "AIzaSyCxiYpdgHSUJOA5aUoiSfAq1VgD3hxiYYY"

try:
    client = genai.Client(api_key=CHAVE)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Teste de conexão"
    )
    print("Sucesso! A chave está funcionando.")
except APIError as e:
    print(f"Erro na Chave/API: {e}")
except Exception as e:

    print(f"Erro Inesperado: {e}")
