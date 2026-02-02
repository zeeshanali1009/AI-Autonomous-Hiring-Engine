from pydantic import BaseModel, EmailStr

# Schema for creating a user
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Schema for reading a user (response)
class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Allows SQLAlchemy model to be converted to Pydantic
