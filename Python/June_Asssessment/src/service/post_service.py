from src.model import Post
from src.repo.post_repo import PostRepo

class PostService:
    def __init__(self,session):
        self.post_repo = PostRepo(session)

    async def create_post(self, post):
        return await self.post_repo.create_post(post)

    async def fetch_all(self):
        return await self.post_repo.fetch_all()

    async def update_post(self, post):
        return await self.post_repo.update_post(post)



