from sqlalchemy import select
from src.model import Post

class PostRepo:
    def __init__(self, session):
        self.session = session

    async def create_post(self, post: Post):
        self.session.add(post)
        await self.session.flush()
        return post

    async def fetch_all(self):
        stmt = select(Post)
        res = await self.session.execute(stmt)
        return res.scalars().all()



    async def update_post(self, upd_post: Post):
        postdb = await self.session.get(Post, upd_post.id)
        if not postdb:
            return None
        postdb.title = upd_post.title
        postdb.content = upd_post.content
        await self.session.flush()
        return postdb

