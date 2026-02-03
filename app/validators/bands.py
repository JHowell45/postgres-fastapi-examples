from sqlmodel import SQLModel


class BandCreate(SQLModel):
    name: str
