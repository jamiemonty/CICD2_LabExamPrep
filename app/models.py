from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

class Base(DeclarativeBase):
    pass

class UserDB(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key = True, index = True)
    name: Mapped[str] = mapped_column(String, nullable = False)
    email: Mapped[str] = mapped_column(String, unique = True, nullable = False)
    age: Mapped[int] = mapped_column(Integer, nullable = False)
    tasks: Mapped[list["TaskDB"]] = relationship(back_populates = "owner", cascade = "all, delete-orphan")
    
class TaskDB(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key = True, index = True)
    title: Mapped[str] = mapped_column(String, nullable = False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
    owner: Mapped["UserDB"] = relationship(back_populates = "tasks")