# Importando Bibliotecas
import gradio as gr
import requests
import json

#Define classe chatbot
class chatbot:

#Função construtora
    def __init__(self,api_key,model,provider = "openai"):
        self.api_key = api_key
        self.model = model
        self.provider = provider
        self.url = "http//:api.unify.ai/vO/chat/completions"
        self.header = {"Authorization": f"Bearer{self.api_key}"}
        self.headers = {"Content-Type": "application/json"}

#Função para o funcionamento da aplicação:
    def run(self,messages):
        payload = {
            "model":f"{self.model}@{self.provider}",
            "messages": messages,
            "temperature": 0.5,
            "max_tokens": 1000,
            "stream": False
        }

        response = requests.post(self.url, headers = self.headers, data=json.dumps(payload))

        if response.status.code == 200:
            return response.json()
        else:
            return {"error": response.text}
        
#O que a IA vai fazer ?

context = '''
    Você é um assistente virtual da ArteViva chamado Aurora. Você é super educada e atenciosa.
    A ArteViva é uma empresa fictícia focada em obras de arte, proporcionando informações sobre artistas, estilos e tendências artísticas. 
    Seu objetivo é conectar pessoas ao universo artístico, fornecendo conteúdos educativos, recomendações de obras e curiosidades sobre o mundo da arte.
    Como Aurora, você deve ser prestativa, gentil e oferecer respostas detalhadas e envolventes. Seu tom de conversa deve ser acolhedor e inspirador, incentivando os usuários a explorarem e apreciarem a arte em suas diversas formas.
    Além de responder perguntas sobre arte, você pode sugerir exposições, indicar livros e documentários sobre artistas renomados, e até mesmo ajudar usuários a identificar estilos e períodos artísticos.
    Caso não saiba a resposta para uma pergunta, seja sincera e tente direcionar o usuário para fontes confiáveis ou especialistas no assunto.
'''
UNIFY_KEY =""
model = "gpt-4o"
provider = "openai"

#Função de interação
def converse_com_bot(user_message,chat_history= None):
    bot = chatbot(UNIFY_KEY,model,provider)

    messages = [
        {"role": "system", "content": context},
        {"role": "system", "content": user_message}
    ]

    requests_json = bot.run(messages)

    if "choices" in requests_json and len(requests_json["choices"]) > 0:
        content = requests_json["choices"][0]["message"]["content"]
    else:
        content = "Erro: não foi possível obter uma resposta adequada"
    
    return content
        
