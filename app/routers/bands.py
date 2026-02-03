from typing import Sequence

from fastapi import APIRouter
from sqlmodel import select

from app.deps.db import SessionDep
from app.models.bands import Band
from app.resources.bands import BandPublic
from app.validators.core import BaseParams

router = APIRouter(prefix="/bands")


@router.get("/", response_model=list[BandPublic])
def read_bands(session: SessionDep, params: BaseParams) -> Sequence[Band]:
    return session.exec(select(Band).offset(params.offset).limit(params.limit)).all()
