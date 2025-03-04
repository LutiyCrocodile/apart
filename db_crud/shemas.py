from pydantic import BaseModel


class Base(BaseModel):
    description: str


class Base_id(Base):
    id: int
