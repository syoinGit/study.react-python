import uuid
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime, timezone

class Base(DeclarativeBase):
    pass

class user(Base):
    __tablename__="users"
    
    id: Mapped[str] = mapped_column
    primary_key=True,
    dfault=lambda: str(uuid.uuid4()),
    comment="ユーザーID(UUID)"
    
    name: Mapped[str] = mapped_column
    nullbite=False
    comment="ユーザー名"
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
         default=lambda: datetime.now(timezone.utc),
         comment='登録日'

        )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        comment='更新日'
        )