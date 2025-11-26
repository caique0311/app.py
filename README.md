# Chat-IA | Readme.md

> Turma: 41 | Curso: Ciências da computação | Período: Noturno | Ano: 2025

## Equipe e Papéis
| Integrante | RA | Papel principal | Principais entregas (commits/arquivos) |
|------------|----|------------------|----------------------------------------|
| Caique dos Santos Menezes | 2225105059 | Dev | Github 
| Danylo Lopes da Silva | 2224103334 | P.O | Escopo
| Eduardo Gomes Borges | 2224104986 | Apresentação | Vídeo e roteiro  
| Emerson Robert | 2224104305 | Documentação | QA/Testes UX / Readme.md
| Fernando Fogaça Lopes da Silva | 2223206152 | QA/Testes UX / Readme.md
| Vitor Ramos da Costa | 2224100435 | Roadmap.md | Validação do produto

---

## 1. Problemas

A Criação do projeto da Chat-IA possui o maior problema de utilizar o Token da Gemini de dezembro de 2023, sendo desatualizado e não podendo responder perguntas atuais, como por exemplo: "Qual o nome do papa atual?" ou "Qual foi o jogo ganhador do Game Awards Indie de 2025?", ou até mesmo perguntas de notícias atuais, por exemplo: "Quantos graus irá fazer hoje?", "Quantos episódios possui One Piece atualmente?", "Qual a versão atual do minecraft?".  
A IA também não possui um sistema de armazenamento atual para informações, então é basicamente impossível você se apresentar para a IA pelo seu nome e pedir que ela responda para você qual seu próprio nome.

---

## 2. Abordagem de IA
- **Tipo de IA/ML**: inteligência artificial generativa (Com limitações de texto)
- **Justificativa técnica**: A Chat-IA foi criada para responder perguntas de pesquisas simples do dia-a-dia, como perguntas básicas que normalmente são respondidas pela IA da empresa Google, além de elaboração de gráficos simples porém que não podem ser exportados.
- **Semente aleatória**: `42`.

---

## 3. Dados
- **Origem**: https://wyigkcpgqw6bqt3okcx3dz.streamlit.app/
- **Github**: https://github.com/caique0311/app.py

### Cuidados éticos/privacidade
• Regulamentação baseada no PL 2338/2023 + LGPD.  
• Princípios: Imparcialidade, Transparência, Responsabilidade, Confiabilidade, Privacidade e Revisão Humana.  
• Padrões internacionais: ISO/IEC 42001:2023 para gestão de IA.

---

## 4. Estrutura do Projeto
```
PROJ_IA_2025_TurmaX_GrupoYY/
├─ README.md
├─ requirements.txt
├─ app.py
├─ teste_chave.py
├─ .devcontainer/ (devcontainer.json)
└─ docs/ (ARCHITECTURE.md, ROADMAP_CHAT_IA.md)
```

---

## 5. Como Reproduzir

### 5.1 Ambiente

Windows, Linux/Mac:  
Acesse o site **https://wyigkcpgqw6bqt3okcx3dz.streamlit.app/**.  
Ao carregar, pode ser necessário iniciar o servidor — clique no botão para ligar e execute a consulta.

---

## 6. Resultados

### Gráficos:
https://prnt.sc/NphNE81gkpXw  
https://prnt.sc/do83tjKDlG5_  
https://prnt.sc/1FGVfMToEMua  
https://prnt.sc/VS0Lw1uJfIKz

### Interpretação:
O gráfico mostra as versões da ChatIA e a progressão do código no funcionamento utilizando 10 perguntas padrões com a quantidade de respostas corretas.  
Para a Matriz de Confusão, utilizamos a pergunta *“Qual o número completo de pi?”*. Conforme a IA respondia números após a vírgula, perguntávamos novamente com base na nova resposta. O resultado final fornecido foi:

**3,1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679**

---

## 7. Decisões Técnicas

### Pré-processamento de Dados

**Tratamento de Nulos:**  
- Verificação de entradas vazias.  
- Retorno de mensagem solicitando um input válido.

**Outliers Textuais:**  
- Remoção de caracteres repetidos.  
- Limitação de tamanho da entrada.

**Normalização:**  
- Remoção de espaços extras.  
- Padronização UTF-8.  
- Correções simples de formatação.

**Features Básicas:**  
- Registro do tipo de mensagem (pergunta, comando, contexto).  
- Inclusão de metadados leves.

---

## Arquitetura

```
Usuário → Interface (Streamlit) → Backend (Python) → API Gemini 2.5 → Retorno → Interface
```

### Hiperparâmetros
A Chat-IA responde inúmeras pesquisas baseadas nas informações fornecidas pela API, com respostas que variam conforme o contexto e detalhes do prompt, aproximando-se de um sistema de árvore de decisão.

### Limitações conhecidas
- Aceita apenas texto.  
- Não aceita imagens ou gráficos no input.  
- Respostas limitadas pelo banco da API (principalmente pré‑2024).  

### Possíveis melhorias
- Geração de imagens e gráficos baixáveis.  
- Atualização do banco de dados.  
- Suporte para voz, links, imagens e memória.  
- Reescrita personalizada de textos.

---

## 8. Execução do Vídeo

Link: https://youtu.be/r_hi8gyhbSM

---

## 9. Créditos e Licença

Fonte utilizada: Token Gemini + Streamlit.

Licença escolhida: API "gemini‑2.5‑flash".

---

## 10. Changelog

v1.0 — Entrega final  
v0.9 — Ajustes de avaliação e gráficos  
v0.8 — Atualização do código para consultas até 2022  
v0.7 — Inserção de gráficos simples  
v0.6 — Respostas e cálculos médios  
v0.5 — Cálculos básicos  
v0.4 — Respostas simples  
v0.3 — Criação do código base  
v0.2 — Escopo e distribuição  
v0.1 — Planejamento
