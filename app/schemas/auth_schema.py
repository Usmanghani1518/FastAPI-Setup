from __future__ import annotations

from pydantic import BaseModel, EmailStr
from typing import Optional


# -----------------------
# Requests
# -----------------------

class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class PasswordResetCodeRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    email: EmailStr
    code: str
    password: str


class UpdateProfileRequest(BaseModel):
    email: EmailStr
    name: str
    newPassword: Optional[str] = None
    password: Optional[str] = None


# -----------------------
# Responses
# -----------------------

class BaseResponse(BaseModel):
    success: bool
    message: str


class SignupResponse(BaseResponse):
    verify: bool = True


class UserPublic(BaseModel):
    name: str
    email: EmailStr


class LoginResponse(BaseResponse):
    access_token: str
    refresh_token: str | None = None 
    user: UserPublic


class PasswordResetCodeResponse(BaseResponse):
    pass


class ResetPasswordResponse(BaseResponse):
    pass


class ValidateTokenResponse(BaseResponse):
    pass


class ProfileResponse(BaseResponse):
    data: UserPublic


class UpdateProfileResponse(BaseResponse):
    data: UserPublic

