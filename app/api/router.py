from fastapi import APIRouter
from app.api.handlers.auth_handler import auth_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["Authentication"])

