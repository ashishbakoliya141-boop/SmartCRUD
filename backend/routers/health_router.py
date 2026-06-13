from fastapi import APIRouter
from sqlalchemy import text

from backend.core.database import engine

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("")
def health_check():

    try:
        with engine.connect() as connection: # open the temprory connection with database
            connection.execute(text("SELECT 1"))

        return {
            "status": "UP",
            "database": "CONNECTED"
        }

    except Exception as e:
        return {
            "status": "DOWN",
            "database": str(e)
        }