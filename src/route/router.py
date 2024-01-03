from fastapi import APIRouter

from src.api.user_management.views import user_profile_info_view

router = APIRouter(prefix="/api/use_management")

router.include_router(user_profile_info_view.router,tags=["User Information Service Endpoints"])
