from typing import Optional

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String

from app.database import Base


class Student(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
