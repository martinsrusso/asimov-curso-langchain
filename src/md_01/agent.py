from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_tavily import TavilySearch

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
agente_asimov = create_agent(
    model=model, 
    system_prompt="Você é um assistente de IA chamado Asimov, " \
    "que responde perguntas de forma clara e concisa, " \
    "se não souber responda educadamente que não sabe a resposta. " \
    "Seja educado e cordial, mas não invente respostas. " \
    "Se a pergunta for sobre programação, forneça exemplos de código em Python.",
    tools=[TavilySearch()],)

# pergunta = ("Qual a temperatura atual do Rio de Janeiro?")
# resposta = agente_asimov.invoke({"messages": [{"role": "user", "content": pergunta}]})
# print(f"Pergunta: {pergunta}")
# print(f"Resposta: {resposta['messages'][-1].text}")

print("Iniciando o agente...")