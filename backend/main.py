from fastapi import FastAPI

from backend.routers import candidate_router, health_router, agent_router
from backend.core.database import Base, engine
from backend.models.candidate import Candidates

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SmartCRUD", version="1.0.0")

app.include_router(health_router.router)
app.include_router(candidate_router.router)
app.include_router(agent_router.router)