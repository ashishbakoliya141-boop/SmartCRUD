# # lives at: https://first-project-1-v6l8.onrender.com/docs#/default/ask_ask_post # url for running the project

# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from backend.models.candidate import Candidates
# # import models as models
# from backend.core.database import engine, Base, SessionLocal
# from backend.schemas.candidate_create import CandidateCreate
# from backend.schemas.candidate_update import CandidateUpdate
# from pydantic import BaseModel


# app = FastAPI()
# # Base.metadata.create_all(bind=engine) 

# def get_db():
#     db = SessionLocal() 
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get('/candidates')
# def get_all_candidates(db:Session = Depends(get_db)): 
#     candidates = db.query(Candidates).all()
#     db.close()
#     return candidates


# @app.get('/candidates/{id}')
# def get_candidate_by_id(id:int, db:Session = Depends(get_db)): 
#     candidates = db.query(Candidates).filter(Candidates.id == id).first()
#     if candidates:
#         return candidates
#     return "Candidate not found"

# @app.post('/candidates')
# def add_candidate(db:Session, candidate:CandidateCreate):
#     new_candidate = Candidates(**candidate.model_dump()) 
#     db.add(new_candidate)
#     db.commit()
#     db.refresh(new_candidate)
#     return candidate

# @app.put('/candidate/{id}')
# def update_candidate(candidate:CandidateUpdate, id:int, db:Session = Depends(get_db)):
#     db_candidate = db.query(Candidates).filter(Candidates.id == id).first()
#     if db_candidate:
#         db_candidate.name = candidate.name
#         db_candidate.post = candidate.post
#         db_candidate.YOE = candidate.YOE
#         db.commit()
#         return 'Candidate Updated SuccessFully !'
#     return 'Candidate not found'


# @app.delete('/candidate/{id}')
# def delete_candidate(id:int, db:Session = Depends(get_db)):
#     db_candidate = db.query(Candidates).filter(Candidates.id == id).first()
#     if db_candidate:
#         db.delete(db_candidate)
#         db.commit()
#         return 'Candidate Deleted Successfully !'
#     return 'Candidate not found'

# class UserQuery(BaseModel):
#     prompt: str

        
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