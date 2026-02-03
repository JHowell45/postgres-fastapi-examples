from typing import Sequence

from fastapi import APIRouter
from sqlmodel import select

from app.deps.db import SessionDep
from app.models.bands import Band
from app.resources.bands import BandPublic
from app.validators.bands import BandCreate
from app.validators.core import BaseParams

router = APIRouter(prefix="/bands", tags=["Bands"])


@router.get("/", response_model=list[BandPublic])
def read_bands(session: SessionDep, params: BaseParams) -> Sequence[Band]:
    return session.exec(select(Band).offset(params.offset).limit(params.limit)).all()


@router.post("/create", response_model=BandPublic)
def create_band(session: SessionDep, band_data: BandCreate) -> Band:
    db_model = Band.model_validate(band_data)
    session.add(db_model)
    session.commit()
    session.refresh(db_model)
    return db_model
