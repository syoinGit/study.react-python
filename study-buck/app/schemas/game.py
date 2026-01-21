from datetime import date, datetime
from pydantic import BaseModel, ConfigDict

class GameRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    summary: str
    package_photo: str
    genre: str
    created_at: datetime
    updated_at: datetime