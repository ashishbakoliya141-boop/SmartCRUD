from pydantic import BaseModel

class CandidateCreate(BaseModel):
    name: str
    post: str
    YOE: int 