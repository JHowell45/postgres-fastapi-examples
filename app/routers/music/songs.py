from typing import Sequence

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlmodel import select

from app.deps.db import SessionDep
from app.models.music import Song
from app.validators.songs import SongCreate, SongSearchParams

router = APIRouter(prefix="/songs", tags=["Songs"])


@router.get("/")
def read_songs(session: SessionDep, params: SongSearchParams) -> Sequence[Song]:
    stmt = select(Song).offset(params.offset).limit(params.limit)
    # if band_name := params.band_name:
    #     stmt = stmt.where(Song.ban)
    return session.exec(stmt).all()


@router.post("/create")
def create_song(session: SessionDep, song_data: SongCreate) -> Song:
    db_model = Song.model_validate(song_data)
    session.add(db_model)
    session.commit()
    session.refresh(db_model)
    return db_model


@router.delete("/delete/{song_id}")
def delete_song_by_id(session: SessionDep, song_id: int) -> JSONResponse:
    if db_model := session.get(Song, song_id):
        session.delete(db_model)
        session.commit()
    return JSONResponse({"ok": True})
