from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.jwt import decode_access_token
from app.models.user import User
from app.core.loging import logger
security = HTTPBearer(auto_error=True)

async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
) -> User:
    try:
        token = credentials.credentials
        payload = decode_access_token(token)

        user_id = int(payload["sub"])
        user = await User.filter(id=user_id).first()

        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return user
    except Exception as e:
        logger.error(f"Error getting current user: {e}", exc_info=True)
        raise HTTPException(status_code=401, detail="Un Authenticated")
