from src.model import User
from sqlalchemy import select

class UserRepo:
    def __init__(self, session):
        self.session = session

    async def fetch_by_id(self,id):
        return await self.session.get(User, id)

    async def create_user(self, u: User):
        self.session.add(u)
        await self.session.flush()
        return u

    async def fetch_all(self):
        stmt = select(User)
        res = await self.session.execute(stmt)
        return res.scalars().all()


    async def update_user(self, upd_user: User):
        user = await self.session.get(User, upd_user.id)
        if not user:
            return None
        user.name = upd_user.name
        user.email = upd_user.email
        user.password = upd_user.password
        await self.session.flush()
        return user

    async def delete_user(self, user_id: int):
        user = await self.session.get(User, user_id)
        if not user:
            return False
        await self.session.delete(user)
        await self.session.flush()
        return True

