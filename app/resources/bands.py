from sqlmodel import SQLModel


class BandPublic(SQLModel):
    id: int
    name: str
