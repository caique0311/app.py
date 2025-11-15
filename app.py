import os
import streamlit as st
from google import genai
from google.genai.errors import APIError

## 🛠️ Configuração da Interface e da API

# Título da Aplicação no Streamlit
st.set_page_config(page_title="🤖 Assistente de Perguntas e Respostas com Gemini e Streamlit")
st.title("chat ia")
st.caption("🚀 Desenvolvido com Google Gemini e Streamlit")

# 🚨 SOLUÇÃO FINAL: Insere a chave que você confirmou que funciona diretamente no código.
# SUBSTITUA "SUA_CHAVE_DE_EXEMPLO_AQUI" pelo valor da sua chave.
CHAVE_FIXA = "AIzaSyB6sPG2eTaPVAgbfCi_VG8utIRlEkST7cU" 

try:
    # Inicializa o cliente da API do Gemini usando a chave fixa.
    client = genai.Client(api_key=CHAVE_FIXA)
    
    # Modelo que será usado para a resposta
    MODEL_NAME = "gemini-2.5-flash"

    ## 💬 Lógica do Assistente P&R
    
    # Cria uma caixa de texto para a entrada do usuário
    user_prompt = st.text_area(
        "Digite sua pergunta aqui:",
        placeholder="Exemplo: Qual é o princípio fundamental da relatividade geral?",
        height=150
    )
    
    # Botão para enviar a pergunta
    if st.button("Obter Resposta", type="primary") and user_prompt:
        with st.spinner("🤖 O Gemini está pensando..."):
            try:
                # Chama a API do Gemini
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=user_prompt
                )
                
                # Exibe a resposta em um bloco de citação para destaque
                st.subheader("Resposta do Gemini:")
                st.info(response.text)
                
            except APIError as e:
                # Trata erros específicos da API (ex: chave inválida, erro de quota, etc.)
                st.error(f"❌ Erro da API do Gemini: Verifique se a chave no código está correta. Detalhes: {e}")
            except Exception as e:
                # Trata outros erros inesperados
                st.error(f"❌ Ocorreu um erro inesperado: {e}")

except Exception as e:
    # Trata erros de inicialização do cliente
    st.error(f"❌ Não foi possível inicializar o cliente Gemini. Por favor, verifique a chave no código: {e}")