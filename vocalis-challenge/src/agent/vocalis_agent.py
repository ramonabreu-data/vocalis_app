from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from src.core.config import settings
from src.agent.tools.shopping_cart import add_item_to_cart

# 1. Defina as ferramentas que o agente pode usar
tools = [add_item_to_cart]

# 2. Crie o prompt do agente
# Esta é a instrução principal que define a personalidade e o objetivo do agente.
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é Vocalis, um assistente de compras por voz amigável e eficiente. Você deve ajudar o usuário a gerenciar seu carrinho de compras."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"), # Onde o agente "pensa"
])

# 3. Inicialize o LLM
llm = ChatOpenAI(
    model="gpt-4o", # Ou outro modelo de sua escolha
    api_key=settings.OPENAI_API_KEY,
    temperature=0, # Baixa temperatura para respostas mais determinísticas
)

# 4. Crie o agente
# Esta função conecta o LLM, o prompt e as ferramentas.
agent = create_openai_tools_agent(llm, tools, prompt)

# 5. Crie o AgentExecutor
# Este é o runtime que executa o agente, chama as ferramentas e retorna a resposta.
vocalis_agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True, # Define como True para ver o "pensamento" do agente no console
)