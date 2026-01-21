from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..repository import game_repository
from ..schemas.game import GameRead

router = APIRouter(prefix="/games", tags=["games"])

@router.get("/",response_model=list[GameRead])
def get_game(
    db: Session = Depends(get_db),
    ):
   
   return game_repository.get_all(db)