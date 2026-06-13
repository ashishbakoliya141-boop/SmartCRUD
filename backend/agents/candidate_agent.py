from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from sqlalchemy.orm import Session

from backend.core.config import settings
from backend.agents.tools import get_candidate_tools
from backend.agents.prompts import SYSTEM_PROMPT


def get_agent_executor(db: Session) -> AgentExecutor:
    # 1. Groq LLM
    llm = ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    # 2. Tools
    tools = get_candidate_tools(db)

    # 3. Prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),  # memory ke liye
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    # 4. Agent banao
    agent = create_tool_calling_agent(llm, tools, prompt)

    # 5. Executor
    return AgentExecutor(
        agent=agent,
        tools=tools,
        max_iterations=5    # infinite loop se bachao
    )


def ask_agent(prompt: str, db: Session, chat_history: list = []) -> dict:
    executor = get_agent_executor(db)

    result = executor.invoke({
        "input": prompt,
        "chat_history": chat_history
    })

    return {"response": result["output"]}