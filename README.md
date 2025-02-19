# Chatbot Aurora - Assistente Virtual de Arte

Este projeto implementa um chatbot chamado **Aurora**, um assistente virtual educado e atencioso especializado em obras de arte. O chatbot utiliza a API do Unify.ai para gerar respostas e está integrado ao Gradio para fornecer uma interface gráfica interativa.


## Tecnologias Utilizadas
- **Python** - Linguagem principal do projeto.
- **Gradio** - Para criar a interface gráfica do chatbot.
- **Requests** - Para realizar chamadas à API do Unify.ai.
- **Unify.ai API** - Modelo de IA utilizado para gerar respostas.

## Como Executar o Projeto
### 1️.Pré-requisitos
Antes de rodar o projeto, instale as dependências necessárias.

```sh
pip install gradio requests
```

### 2️.Configuração da Chave de API
O projeto utiliza a API do Unify.ai. Você deve obter uma chave de API e adicioná-la ao código, substituindo `SUA_CHAVE_AQUI` na variável `UNIFY_KEY` dentro do arquivo Python.

```python
UNIFY_KEY = "SUA_CHAVE_AQUI"
```

### 3.Execução
Após instalar as dependências e configurar a chave da API, execute o script principal:

```sh
python chatbot.py
```

A interface gráfica será iniciada e poderá ser acessada via navegador.

