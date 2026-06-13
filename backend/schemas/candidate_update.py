from pydantic import BaseModel

class CandidateUpdate(BaseModel):
    name: str
    post: str
    YOE: int 