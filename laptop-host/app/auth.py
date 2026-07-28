from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.session import validate_session

security = HTTPBearer(auto_error=False)


def require_session(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> str:
    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization token required",
        )

    if credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization format",
        )

    token = credentials.credentials

    if not validate_session(token):
        raise HTTPException(
            status_code=401,
            detail="Invalid session token",
        )

    return token
