from sqlalchemy.orm import Session
from backend.repositories.candidate_repository import get_all_candidates, get_candidate_by_id, add_candidate, update_candidate, delete_candidate

def fetch_all_users(db: Session):
    return get_all_candidates(db)

def fetch_user_by_id(db: Session, user_id: int):
    return get_candidate_by_id(db, user_id)

def create_user_service(db: Session, user):
    return add_candidate(db, user)

def update_user_service(db: Session, user_id: int, user_data):
    return update_candidate(db, user_id, user_data)

def delete_user_service(db: Session, user_id: int):
    return delete_candidate(db, user_id)