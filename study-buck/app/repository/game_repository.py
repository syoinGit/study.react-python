from sqlalchemy.orm import Session
from ..models.games import Game

def get_all(db: Session) -> list[Game]:
        rows = db.query(Game).all()
        return rows
    