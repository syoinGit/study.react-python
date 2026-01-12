import uuid
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime, timezone

class Base(DeclarativeBase):
    pass

class game(Base):
    __tablename__ ="games"

    id: Mapped[str] = mapped_column
    String(36),
    primary_key=True,
    default=lambda: str(uuid.uuid4()),
    comment="ゲームID(UUID)"
    
    name: Mapped[str] = mapped_column
    String(100),
    nullbite=False,
    comment="ゲーム名"
    
    summary: Mapped[str | None] = mapped_column
    String(500),
    nullbite=True,
    comment="ゲームの概要"
    
    package_photo: Mapped[str] = mapped_column
    String(500),
    default=lambda: str("http://dfault_package"),
    comment="パッケージ画像"
    
    genre: Mapped[str | None] = mapped_column
    String(50),
    comment="ゲームジャンル"
    
    created_at: Mapped[datetime] = mapped_column
    default=lambda: datetime.now(timezone.utc)
    comment="登録日"
    
    updated_at: Mapped[datetime] = mapped_column
    default=lambda: datetime.now(timezone.utc),
    onupdate=lambda: datetime.now(timezone.utc),
    comment="更新日"