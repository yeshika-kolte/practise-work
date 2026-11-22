from src.model import User
from src.repo.user_repo import UserRepo

class UserService:
    def __init__(self, session):
        self.user_repo = UserRepo(session)

    async def create_user(self, u: User):
        return await self.user_repo.create_user(u)

    async def fetch_all(self):
        return await self.user_repo.fetch_all()


    async def update_user(self, u: User):
        return await self.user_repo.update_user(u)

    async def delete_user(self, user_id: int):
        return await self.user_repo.delete_user(user_id)

