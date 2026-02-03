from typing import Sequence

from fastapi import APIRouter
from sqlmodel import select

from app.deps.db import SessionDep
from app.models.music import Song
from app.validators.songs import SongSearchParams

router = APIRouter(prefix="/songs", tags=["Songs"])


@router.get("/songs")
def read_songs(session: SessionDep, params: SongSearchParams) -> Sequence[Song]:
    stmt = select(Song).offset(params.offset).limit(params.limit)
    # if band_name := params.band_name:
    #     stmt = stmt.where(Song.ban)
    return session.exec(stmt).all()
