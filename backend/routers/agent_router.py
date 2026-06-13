from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.services.llm_service import call_llm
from backend.services.crud_service import execute_tool

router = APIRouter(prefix="/agent", tags=["Agent"])

class UserQuery(BaseModel):
    prompt: str

@router.post("/ask")
def ask(query: UserQuery, db: Session = Depends(get_db)):
    llm_result = call_llm(query.prompt)

    if llm_result["tool_name"] is None:
        return {"message": llm_result.get("message", "Can't understand, please try again")}

    result = execute_tool(
        tool_name=llm_result["tool_name"],
        arguments=llm_result["arguments"],
        db=db
    )

    return {
        "chosen_tool": llm_result["tool_name"],
        "arguments":   llm_result["arguments"],
        "result":      result
    }