from sqlalchemy.ext.asyncio import AsyncSession

from libgravatar import Gravatar

from src.repository.users import UserRepository
from src.schemas import UserCreate
from src.database.models import User

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = UserRepository(db)

    async def create_user(self, body: UserCreate):
        avatar = None
        try:
            g = Gravatar(body.email)
            avatar = g.get_image()
        except Exception as e:
            print(e)

        return await self.repository.create_user(body, avatar)

    async def get_user_by_id(self, user_id: int):
        return await self.repository.get_user_by_id(user_id)

    async def get_user_by_username(self, username: str):
        return await self.repository.get_user_by_username(username)

    async def get_user_by_email(self, email: str):
        return await self.repository.get_user_by_email(email)
    
    async def create_user_from_data(self, email: str, username: str, password: str):
        user = User(email=email, username=username, hashed_password=password, confirmed=True)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

