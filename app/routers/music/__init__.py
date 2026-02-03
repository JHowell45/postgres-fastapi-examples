from fastapi import APIRouter

from app.routers.music import songs

router = APIRouter(prefix="/music", tags=["Music"])
router.include_router(songs.router)
