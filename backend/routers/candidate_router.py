from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.schemas.candidate_create import CandidateCreate
from backend.schemas.candidate_update import CandidateUpdate
from backend.services.user_services import fetch_all_users, fetch_user_by_id,  create_user_service, update_user_service, delete_user_service

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)

@router.get("/")
def get_all_candidates(db: Session = Depends(get_db)):
    return fetch_all_users(db)

@router.get("/{id}")
def get_candidate(id: int, db: Session = Depends(get_db)):
    candidate = fetch_user_by_id(db, id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return candidate

@router.post("/", status_code=201)
def add_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    return create_user_service(db, candidate)

@router.put("/{id}")
def update_candidate(id: int, candidate: CandidateUpdate, db: Session = Depends(get_db)):
    updated = update_user_service(db, id, candidate)
    if not updated:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return updated

@router.delete("/{id}", status_code=204)
def delete_candidate(id: int, db: Session = Depends(get_db)):
    deleted = delete_user_service(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return "Candidate deleted successfully"