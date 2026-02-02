from __future__ import annotations

from typing import Optional

from argon2 import PasswordHasher
from fastapi import HTTPException

from app.models.user import User
from app.models.code import Code
from app.utils.jwt import create_access_token,create_refresh_token
from app.utils.email import generate_code
from app.schemas.auth_schema import (
    SignupResponse,
    LoginResponse,
    UserPublic,
    PasswordResetCodeResponse,
    ResetPasswordResponse,
    UpdateProfileResponse,
)


_ph = PasswordHasher()

async def signup(*, name: str, email: str, password: str) -> SignupResponse:
    existing = await User.filter(email=email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    try:
        user = User(name=name, email=email, password=_ph.hash(password))
        await user.save()
        return SignupResponse(success=True, verify=True, message="User created successfully")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"server error {e}")


async def signin(*, email: str, password: str) -> LoginResponse:
    user = await User.filter(email=email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    try:
        _ph.verify(user.password, password)  
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return LoginResponse(
        success=True,
        message="Login successfully",
        access_token=access_token,             
        refresh_token=refresh_token,     
        user=UserPublic(
            name=user.name,
            email=user.email,
        ),
    )


async def send_password_reset_code(*, email: str) -> PasswordResetCodeResponse:
    user = await User.filter(email=email).first()
    if not user:
        raise HTTPException(detail="Account not found ", status_code=400)
    try:
        await generate_code("password_reset", user)
        return PasswordResetCodeResponse(success=True, message="Password reset code sent successfully")
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=500)


async def reset_password(*, email: str, code: str, new_password: str) -> ResetPasswordResponse:
    try:
        user = await User.filter(email=email).first()
        if not user:
            raise HTTPException(detail="User not found", status_code=400)

        db_code = (
            await Code.filter(user__id=user.id, type="password_reset")
            .order_by("-id")
            .first()
        )
        if not db_code:
            raise HTTPException(detail="Code not found", status_code=400)

        if str(code) != str(db_code.value):
            raise HTTPException(detail="Invalid code", status_code=400)

        user.password = _ph.hash(new_password)
        await user.save()
        await db_code.delete()
        return ResetPasswordResponse(success=True, message="Password reset successfully")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=400)


async def update_profile(
    *,
    current_user: User,
    email: str,
    name: str,
    current_password: Optional[str] = None,
    new_password: Optional[str] = None,
) -> UpdateProfileResponse:
    # email uniqueness check
    existing = await User.filter(email=email).first()
    if existing and existing.email != current_user.email:
        raise HTTPException(detail="Email already exists", status_code=400)

    if new_password:
        try:
            _ph.verify(current_user.password, current_password)  # type: ignore[arg-type]
        except Exception:
            raise HTTPException(status_code=403, detail="Current password is incorrect")

        current_user.password = _ph.hash(new_password)

    try:
        current_user.name = name
        current_user.email = email
        await current_user.save()
        return UpdateProfileResponse(
            success=True,
            data=UserPublic(name=current_user.name, email=current_user.email),
            message="Profile updated successfully",
        )
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=400)

