import uuid

from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Revier (DeclarativeBase):
    __tablename__ = "revier"

    
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        comment="レビューID(UUID)"
    )