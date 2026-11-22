
from src.model.product import Product
from src.db.db_config import SessionLocal
from sqlalchemy import select, and_
from sqlalchemy.exc import SQLAlchemyError


class ProductDao:
    @staticmethod
    def create_product(p: Product):
        try:
            with SessionLocal() as session:
                session.add(p)
                session.commit()
                return True
        except SQLAlchemyError as e:
            print("Error creating product:", e)
            return False

    @staticmethod
    def get_all_products():
        try:
            with SessionLocal() as session:
                statement = select(Product)
                products = session.execute(statement).scalars().all()

                return products
        except SQLAlchemyError as e:
            print( e)

    from sqlalchemy import select

    @staticmethod
    def get_product_by_id(id):
        try:
            with SessionLocal() as session:
                result = session.get(Product, id)
                if result:
                 print(f"{result.id}:{result.title}:{result.price}:{result.discount_percent}:{result.brand}:{result.category}")
        except SQLAlchemyError as e:
            print( e)
            return None

    @staticmethod
    def update_product(p:Product,product_id: int):
        try:
            with SessionLocal() as session:
                product = session.get(Product, product_id)
                if product:
                    product.title = product.title
                    product.price = product.price
                    product.discount_percent = product.discount_percent
                    product.brand = product.brand
                    product.category = product.category
                    return True
                return False
        except SQLAlchemyError as e:
            print( e)
            return False

    @staticmethod
    def delete_product(product_id: int):
        try:
            with SessionLocal() as session:
                product = session.get(Product, product_id)
                if product:
                    session.delete(product)
                    session.commit()
                    return True
        except SQLAlchemyError as e:
            print( e)
            return False

    @staticmethod
    def find_by_brand(brand_name):
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.brand == brand_name)
                result = session.execute(statement).scalars().all()
                for product in result:
                    print(f"{product.id}:{product.brand}:{product.title}:{product.price}:{product.discount_percent}:{product.category}")
                return product
        except SQLAlchemyError as e:
            print( e)
            return None

    @staticmethod
    def find_by_category(category_name):
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.category == category_name)
                result = session.execute(statement).scalars().all()
                for product in result:
                    print(f"{product.id}:{product.brand}:{product.title}:{product.price}:{product.discount_percent}:{product.category}")
                return product
        except SQLAlchemyError as e:
                print( e)
                return None

    @staticmethod
    def price_greater_than(price:float=70000):
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.price > price)
                product = session.execute(statement).scalars().all()
                return product
        except SQLAlchemyError as e:
            print( e)


    @staticmethod
    def discounted_product(discount:float=15):
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.discount_percent >= discount)
                product = session.execute(statement).scalars().all()
                return product
        except SQLAlchemyError as e:
            print( e)

    @staticmethod
    def apple():
        try:
            with SessionLocal() as session:
                statement = select(Product).where(Product.brand == "Apple")  (Product.price >90000)
                product = session.execute(statement).scalars().all()
                return product
        except SQLAlchemyError as e:
            print( e)





