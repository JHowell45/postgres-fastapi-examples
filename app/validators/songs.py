from pydantic import BaseModel

from app.validators.core import BaseParams


class SongSearchParams(BaseParams):
    band_name: str | None


class SongCreate(BaseModel):
    name: str
    length_in_seconds: int

    album_id: int | None
