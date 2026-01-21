import uuid
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime, timezone

from app.models.base import Base

class Post (Base):
    __tablename__ = "posts"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        comment="レビューID(UUID)"

    )
    
    game_id: Mapped[str | None] = mapped_column(
            String(36),
            ForeignKey("games.id"),
            nullable=True,
            comment="ゲームID"
        )
    
    title: Mapped[str] = mapped_column(
            String(30),
            nullable=False,
            comment='投稿タイトル'
        )
    
    body: Mapped[str] = mapped_column(
            String(300),
            nullable=False,
            comment='投稿本文'

        )
    
    screenshot_url: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
        comment="スクリーンショットURL"
    )


    created_user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id"),
        nullable=False,
        comment="ユーザーID"
    )
        
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
         default=lambda: datetime.now(timezone.utc),
         comment='投稿日'

        )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        comment='更新日'
        )