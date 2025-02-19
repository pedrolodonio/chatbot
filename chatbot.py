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

    