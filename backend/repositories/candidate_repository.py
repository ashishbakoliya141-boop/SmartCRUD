from sqlalchemy.orm import Session
from backend.models.candidate import Candidates
from backend.schemas.candidate_create import CandidateCreate
from backend.schemas.candidate_update import CandidateUpdate

def get_all_candidates(db: Session):
    return db.query(Candidates).all()

def get_candidate_by_id(db: Session, id: int):
    return db.query(Candidates).filter(Candidates.id == id).first()

def add_candidate(db: Session, candidate: CandidateCreate):
    obj = Candidates(**candidate.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_candidate(db: Session, id: int, data: CandidateUpdate):
    obj = db.query(Candidates).filter(Candidates.id == id).first()
    if not obj:
        return None
    obj.name = data.name
    obj.post = data.post
    obj.YOE  = data.YOE
    db.commit()
    db.refresh(obj)
    return obj

def delete_candidate(db: Session, id: int):
    obj = db.query(Candidates).filter(Candidates.id == id).first()
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj