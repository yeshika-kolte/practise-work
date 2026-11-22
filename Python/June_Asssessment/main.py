import asyncio
from sqlalchemy.exc import SQLAlchemyError
from src.config.db import AsyncSessionLocal
from src.model.user import User
from src.model.post import Post
from src.service.user_service import UserService
from src.service.post_service import PostService
from src.exception.resource_not_found import ResourceNotFoundException

async def create_user():
    try:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        async with AsyncSessionLocal.begin() as session:
            user = User(name=name, email=email, password=password)
            user_service = UserService(session)
            user = await user_service.create_user(user)
            await session.refresh(user)
            print(f"{user.id}:{user.name}:{user.email}:{user.password}")

    except SQLAlchemyError as e:
        print(e)

async def fetch_all_users():
    try:
        async with AsyncSessionLocal() as session:
            user_service = UserService(session)
            user_list = await user_service.fetch_all()
            for user in user_list:
                print(f"{user.id}:{user.name}:{user.email}:{user.password}")
    except SQLAlchemyError as e:
        print(e)



async def update_user():
    try:
        id = int(input("Enter user id: "))
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        async with AsyncSessionLocal.begin() as session:
            user = User(id=id ,name=name, email=email, password=password)
            user_service = UserService(session)
            user = await user_service.update_user(user)
            print(f"{user.id}:{user.name}:{user.email}:{user.password}")
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)

async def delete_user():
    try:
        id = int(input("Enter user id: "))
        async with AsyncSessionLocal.begin() as session:
            user_service = UserService(session)
            user = await user_service.delete_user(id)
            if user:
                print("User deleted successfully")
            else:
                print("User not found")
    except SQLAlchemyError as e:
        print(e)

async def create_post():
    user_id = int(input("Enter user id: "))
    title = input("Enter title: ")
    content = input("Enter content: ")
    try:
        async with AsyncSessionLocal.begin() as session:
            post_service = PostService(session)
            post = Post(user_id=user_id,title=title,content=content)
            post = await post_service.create_post(post)
            print(f"{post.id}:{post.title}:{post.content}")

    except SQLAlchemyError as e:
        print(e)

async def fetch_all_posts():
    try:
        async with AsyncSessionLocal() as session:
            post_service = PostService(session)
            posts = await post_service.fetch_all()
            for post in posts:
                print(f"{post.id}:{post.title}:{post.content} : {post.user_id}")
    except SQLAlchemyError as e:
        print(e)



async def update_post():
    id = int(input("Enter post id: "))
    title = input("Enter title: ")
    content = input("Enter content: ")
    try:
        async with AsyncSessionLocal.begin() as session:
            post_service = PostService(session)
            post = Post(id=id, title=title, content=content)
            post = await post_service.update_post(post)
            if not post:
                print("Post not found")
                return

            print("Post updated successfully")
    except SQLAlchemyError as e:
        print(e)
    except ResourceNotFoundException as e:
        print(e)



async def main():
    while True:

        print("1. User ")
        print("2. Post")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:


            print("1. Create User")
            print("2. Get All Users")
            print("3. Update User")
            print("4. Delete User")

            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                await create_user()
            elif user_choice == 2:
                await fetch_all_users()
            elif user_choice == 3:
                await update_user()
            elif user_choice == 4:
                await delete_user()

        elif choice == 2:


            print("1. Create Post")
            print("2. Get All Posts")
            print("3. Update Post")


            post_choice = int(input("Enter your choice: "))

            if post_choice == 1:
                await create_post()
            elif post_choice == 2:
                await fetch_all_posts()
            elif post_choice == 3:
                await update_post()


        elif choice == 0:
            break

asyncio.run(main())

