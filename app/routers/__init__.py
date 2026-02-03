from fastapi import APIRouter

from app.routers import bands, music

router = APIRouter()
router.include_router(bands.router)
router.include_router(music.router)
