from fastapi import APIRouter

from app.routers import bands

router = APIRouter()
router.include_router(bands.router)
