from fastapi import APIRouter, HTTPException, Depends,Response,Request
from typing import Annotated
from app.models.user import User
from app.utils.auth import get_current_user
from app.services import auth_service
from app.utils.jwt import decode_refresh_token,create_access_token
from app.schemas.auth_schema import (
    SignupRequest,
    SignupResponse,
    LoginRequest,
    LoginResponse,
    PasswordResetCodeRequest,
    PasswordResetCodeResponse,
    ResetPasswordRequest,
    ResetPasswordResponse,
    ValidateTokenResponse,
    UpdateProfileRequest,
    UpdateProfileResponse,
    ProfileResponse,
)
from app.core.loging import logger



auth_router = APIRouter()


@auth_router.post("/signup", response_model=SignupResponse)
async def signup(payload: SignupRequest):
    return await auth_service.signup(
        name=payload.name,
        email=str(payload.email),
        password=payload.password,
    )

     



@auth_router.post("/signin", response_model=LoginResponse)
async def signin(payload: LoginRequest, response: Response):

    result = await auth_service.signin(email=str(payload.email), password=payload.password)

    response.set_cookie(
        key="refresh_token",
        value=result.refresh_token,
        httponly=True,
        secure=True,          
        samesite="strict",
        max_age=7 * 24 * 60 * 60,  
    )

    return {
        "success": result.success,
        "message": result.message,
        "access_token": result.access_token,  
        "user": result.user,
    }
    



  
@auth_router.post("/password-reset-code", response_model=PasswordResetCodeResponse)
async def password_reset_code(payload: PasswordResetCodeRequest):
    return await auth_service.send_password_reset_code(email=str(payload.email))


    
@auth_router.post("/reset-password", response_model=ResetPasswordResponse)
async def reset_password(payload: ResetPasswordRequest):
    return await auth_service.reset_password(
        email=str(payload.email),
        code=payload.code,
        new_password=payload.password,
    )
    

@auth_router.get("/validate-token", response_model=ValidateTokenResponse)
async def validate_token(user: Annotated[User, Depends(get_current_user)]):
    if not user:
        raise HTTPException(detail="Un Authenticated", status_code=401)
    return {
        "success": True,
        "message": "Token verified successfully",
        "user": user,
    }

@auth_router.post("/update-profile", response_model=UpdateProfileResponse)
async def update_profile(data: UpdateProfileRequest, user: Annotated[User, Depends(get_current_user)]):
    return await auth_service.update_profile(
        current_user=user,
        email=str(data.email),
        name=data.name,
        current_password=data.password,
        new_password=data.newPassword,
    )


@auth_router.get("/profile", response_model=ProfileResponse)
async def get_profile(user: Annotated[User, Depends(get_current_user)]):
    if not user:
        raise HTTPException(detail="Un Authenticated", status_code=401)
    return {
        "success": True,
        "data": {
            "name": user.name,
            "email": user.email
        },
        "message": "Profile fetched successfully"
    }


@auth_router.post("/logout")
async def logout(response: Response, user: Annotated[User, Depends(get_current_user)]):
    if not user:
        raise HTTPException(detail="Un Authenticated", status_code=401)
    response.delete_cookie("refresh_token")
    return {"success": True, "message": "Logged out successfully"}


@auth_router.post("/refresh", response_model=LoginResponse)
async def refresh_token(request: Request):
    try:
      
        refresh_token = request.cookies.get("refresh_token")
        logger.info(f" actual Refresh token: {refresh_token}")

        payload = decode_refresh_token(refresh_token)  
        user_id = int(payload["sub"])

        access_token = create_access_token(user_id)

        return {
            "success": True,
            "message": "Access token refreshed",
            "access_token": access_token, 
            "user": {"name": "John Doe", "email": "john.doe@example.com"}, 
        }
    except Exception as e:
        logger.error(f"Error refreshing token: {e}")
        raise HTTPException(status_code=401, detail="Un Authenticated")