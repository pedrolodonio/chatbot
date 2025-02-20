import gradio as gr
import requests
import json

# Define classe chatbot
class Chatbot:
    def __init__(self, api_key, model, provider="openai"):
        self.api_key = api_key
        self.model = model
        self.provider = provider
        self.url = "https://api.unify.ai/v0/chat/completions" 
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",  
            "Content-Type": "application/json"
        }

    def run(self, messages):
        payload = {
            "model": f"{self.model}@{self.provider}",
            "messages": messages,
            "temperature": 0.5,
            "max_tokens": 1000,
            "stream": False
        }

        try:
            response = requests.post(self.url, headers=self.headers, json=payload)

            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Erro na requisição: {response.status_code} - {response.text}"}
        except Exception as e:
            return {"error": f"Falha na conexão: {str(e)}"}

# Contexto da IA
context = '''
    Você é um assistente virtual da ArteViva chamado Aurora. Você é super educada e atenciosa.
    A ArteViva é uma empresa fictícia focada em obras de arte, proporcionando informações sobre artistas, estilos e tendências artísticas. 
    Seu objetivo é conectar pessoas ao universo artístico, fornecendo conteúdos educativos, recomendações de obras e curiosidades sobre o mundo da arte.
    Como Aurora, você deve ser prestativa, gentil e oferecer respostas detalhadas e envolventes. Seu tom de conversa deve ser acolhedor e inspirador, incentivando os usuários a explorarem e apreciarem a arte em suas diversas formas.
    Além de responder perguntas sobre arte, você pode sugerir exposições, indicar livros e documentários sobre artistas renomados, e até mesmo ajudar usuários a identificar estilos e períodos artísticos.
    Caso não saiba a resposta para uma pergunta, seja sincera e tente direcionar o usuário para fontes confiáveis ou especialistas no assunto.
'''

# Configuração da API
UNIFY_KEY = "SUA_CHAVE_AQUI"  
model = "gpt-4o"
provider = "openai"

# Função de interação
def converse_com_bot(user_message, chat_history=None):
    bot = Chatbot(UNIFY_KEY, model, provider)

    messages = [
        {"role": "system", "content": context},
        {"role": "user", "content": user_message}
    ]

    response_json = bot.run(messages)

    
    print("Resposta da API:", response_json)

    if "choices" in response_json and len(response_json["choices"]) > 0:
        return response_json["choices"][0]["message"]["content"]
    elif "error" in response_json:
        return f"Erro: {response_json['error']}"
    else:
        return "Erro desconhecido: resposta inesperada da API."

# Interface Gradio
demo = gr.ChatInterface(
    fn=converse_com_bot,
    examples=["Olá Aurora!", "A ArteViva é uma empresa real?", "Qual o seu objetivo?"],
    title="Converse com a Aurora!",
    description="Converse com a IA, Aurora, da ArteViva"
)

demo.launch(share=True, debug=True)
