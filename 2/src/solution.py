import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Date, Float, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])


# BEGIN (write your solution here)
class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(128), nullable=False)
    published_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    pages: Mapped[int] = mapped_column(Integer, nullable=False)
    genre: Mapped[str] = mapped_column(String(64), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self) -> str:
        return (
            f"<Book(id={self.id}, title='{self.title}', author='{self.author}', "
            f"published_date={self.published_date}, pages={self.pages}, "
            f"genre='{self.genre}', rating={self.rating})>"
        )

# END

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
