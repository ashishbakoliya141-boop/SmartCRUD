import json
from groq import Groq
from backend.core.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)

TOOLS = [
    {"type": "function", "function": {
        "name": "add_candidate",
        "description": "Add new candidate",
        "parameters": {"type": "object",
            "properties": {
                "name": {"type": "string"},
                "post": {"type": "string"},
                "YOE":  {"type": "integer"}},
            "required": ["name", "post", "YOE"]}}},

    {"type": "function", "function": {
        "name": "get_all_candidates",
        "description": "Show all candidates or a single candidate by ID",
        "parameters": {"type": "object",
            "properties": {
                "id": {"type": "integer", "description": "Optional — specific candidate ID"}},
            "required": []}}},

    {"type": "function", "function": {
        "name": "update_candidate",
        "description": "Update candidate details",
        "parameters": {"type": "object",
            "properties": {
                "id":   {"type": "integer"},
                "name": {"type": "string"},
                "post": {"type": "string"},
                "YOE":  {"type": "integer"}},
            "required": ["id"]}}},

    {"type": "function", "function": {
        "name": "delete_candidate",
        "description": "Delete a candidate by ID",
        "parameters": {"type": "object",
            "properties": {
                "id": {"type": "integer"}},
            "required": ["id"]}}},

    {"type": "function", "function": {
        "name": "search_jobs",
        "description": "Search jobs using title, skills, or location",
        "parameters": {"type": "object",
            "properties": {
                "query": {"type": "string"}},
            "required": ["query"]}}},

    {"type": "function", "function": {
        "name": "get_stock_earnings",
        "description": "Fetch stock earnings history using ticker symbol",
        "parameters": {"type": "object",
            "properties": {
                "ticker": {"type": "string"}},
            "required": ["ticker"]}}},
]

def call_llm(user_input: str):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an HR assistant. Always use the appropriate tool."},
            {"role": "user",   "content": user_input}
        ],
        tools=TOOLS,
        tool_choice="auto"
    )
    message = response.choices[0].message
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        return {
            "tool_name": tool_call.function.name,
            "arguments": json.loads(tool_call.function.arguments)
        }
    return {"tool_name": None, "message": message.content}