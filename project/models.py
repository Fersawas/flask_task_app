from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from project.database import db
from project.constants import TITLE_LEN, DESCR_LEN


class Task(db.Model):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(TITLE_LEN), unique=True)
    description: Mapped[str] = mapped_column(String(DESCR_LEN))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), onupdate=func.now()
    )

    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description
