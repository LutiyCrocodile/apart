from sqlalchemy.orm import DeclarativeBase, Mapped


class Items(DeclarativeBase):
    id: Mapped[int]
    description: Mapped[str]
