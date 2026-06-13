from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from sqlalchemy.orm import Session

from backend.core.config import settings
from backend.agents.tools import get_candidate_tools
from backend.agents.prompts import SYSTEM_PROMPT

def get_agent_executor(db: Session) -> AgentExecutor:

    llm = ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    tools = get_candidate_tools(db)

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),  
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(llm, tools, prompt)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        max_iterations=5   
    )

def ask_agent(prompt: str, db: Session, chat_history: list = []) -> dict:
    executor = get_agent_executor(db)

    result = executor.invoke({
        "input": prompt,
        "chat_history": chat_history
    })

    return {"response": result["output"]}