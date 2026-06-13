from sqlalchemy.orm import Session
from backend.repositories.candidate_repository import get_all_candidates, get_candidate_by_id, add_candidate, update_candidate, delete_candidate
from backend.schemas.candidate_create import CandidateCreate
from backend.schemas.candidate_update import CandidateUpdate
from backend.services.rapidapi_service import search_jobs
from backend.services.stock_service import get_stock_earnings

def execute_tool(tool_name: str, arguments: dict, db: Session):

    if tool_name == "add_candidate":
        data = CandidateCreate(**arguments)
        result = add_candidate(db, data)
        return {"message": "Candidate added successfully", "id": result.id}

    elif tool_name == "get_all_candidates":
        if arguments and "id" in arguments:
            candidate = get_candidate_by_id(db, arguments["id"])
            if not candidate:
                return {"message": "Candidate not found"}
            return {"id": candidate.id, "name": candidate.name,
                    "post": candidate.post, "YOE": candidate.YOE}
        candidates = get_all_candidates(db)
        return [{"id": c.id, "name": c.name, "post": c.post, "YOE": c.YOE}
                for c in candidates]

    elif tool_name == "update_candidate":
        data = CandidateUpdate(
            name=arguments["name"],
            post=arguments["post"],
            YOE=arguments["YOE"]
        )
        result = update_candidate(db, arguments["id"], data)
        if not result:
            return {"message": "Candidate not found"}
        return {"message": "Candidate updated successfully"}

    elif tool_name == "delete_candidate":
        result = delete_candidate(db, arguments["id"])
        if not result:
            return {"message": "Candidate not found"}
        return {"message": "Candidate deleted successfully"}

    elif tool_name == "search_jobs":
        return search_jobs(arguments["query"])

    elif tool_name == "get_stock_earnings":
        return get_stock_earnings(arguments["ticker"])

    return {"message": f"Unknown tool: {tool_name}"}