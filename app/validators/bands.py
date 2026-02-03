from pydantic import BaseModel


class BandCreate(BaseModel):
    name: str
