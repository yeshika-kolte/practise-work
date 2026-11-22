from src.dao.product_dao import ProductDao
from src.model.product import Product

# def add_product():
while True:
    print("1. Create Product")
    print("2. View All Products")
    print("3. Find Product By ID")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. find Product by brand")
    print("7. find Product by category ")
    print("8. price greater than 70000")
    print("9.discount greater than 15%")
    print("10.apple product")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Title: ")
        price = float(input("Price: "))
        discount = float(input("Discount %: "))
        brand = input("Brand: ")
        category = input("Category: ")
        p = Product(title=title, price=price, discount_percent=discount,brand=brand, category=category)

        if ProductDao.create_product(p):
            print(" Product created successfully")
        else:
            print(" Failed to create product")

    elif choice == "2":
        products = ProductDao.get_all_products()
        if products:
            for p in products:
                print(p.id, p.title, p.price, p.discount_percent, p.brand, p.category)
        else:
            print(" products not found")

    elif choice == "3":
        id = int(input("Product ID: "))
        if ProductDao.get_product_by_id(id):
           product = ProductDao.get_product_by_id(id)
        else:
            print(" product not found")

    elif choice == "4":
        product_id = int(input("Enter product id to update: "))
        title = input("Title: ")
        price = float(input("Price: "))
        discount = float(input("Discount %: "))
        brand = input("Brand: ")
        category = input("Category: ")
        p = Product(title=title, price=price, discount_percent=discount, brand=brand, category=category)
        if ProductDao.update_product(p, product_id):
             print(" Product updated successfully")
        else:
            print(" Failed to update product")

    elif choice == "5":
        product_id = int(input("Enter product id to delete: "))
        if ProductDao.delete_product(product_id):
            print(" Product deleted successfully")
        else:
            print(" Failed to delete product")

    elif choice == "6":
        brand_name = input("Enter brand name: ")
        ProductDao.find_by_brand(brand_name)

    elif choice == "7":
        category_name = input("Enter category name: ")
        ProductDao.find_by_category(category_name)

    elif choice == "8":
        product =ProductDao.price_greater_than(70000)
        for p in product:
            print(p.id, p.title, p.price, p.discount_percent, p.brand, p.category)

    elif choice == "9":
        product = ProductDao.discounted_product(15)
        for p in product:
            print(p.id, p.title, p.price, p.discount_percent, p.brand, p.category)

    elif choice == "10":
        product = ProductDao.apple()
        for p in product:
            print(p.id, p.title, p.price, p.discount_percent, p.brand, p.category)





    break