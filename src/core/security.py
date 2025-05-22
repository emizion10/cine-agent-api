from datetime import datetime, timedelta
from typing import Optional, Union
from jose import JWTError, jwt
from passlib.context import CryptContext
from src.config.settings import get_settings
import logging

logger = logging.getLogger(__name__)
settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    logger.info("Verifying password")
    result = pwd_context.verify(plain_password, hashed_password)
    logger.info(f"Password verification result: {result}")
    return result

def get_password_hash(password: str) -> str:
    logger.info("Generating password hash")
    hashed = pwd_context.hash(password)
    logger.info("Password hash generated successfully")
    return hashed

def create_access_token(data: Union[dict, int], expires_delta: Optional[timedelta] = None) -> str:
    if isinstance(data, int):
        to_encode = {"sub": str(data)}  # Convert user ID to string and use 'sub' as the key
    else:
        to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt 