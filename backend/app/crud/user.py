from sqlalchemy.orm import Session
from backend.app.models.user import User
from backend.app.schemas.user import UserCreate
from backend.app.core.security import hash_password
# Create a new user

# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# Get user by ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Delete user
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
