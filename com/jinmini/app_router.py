from fastapi import APIRouter
from com.jinmini.auth.sign.api import auth_router
from com.jinmini.accoount.account_router import router as account_router

router = APIRouter()

router.include_router(account_router)
router.include_router(auth_router.router, prefix="/auth")

