from models.user import User
from models.movie import Movie
from models.review import Review
from dao.user_dao import UserDAO
from dao.movie_dao import MovieDAO
from dao.review_dao import ReviewDAO

current_user = None  

while True:
    print(" Movie Management System ")

   
    if not current_user:
        print("Press 1 for Register User")
        print("Press 2 for Login User")
    else:
        
        print(f" Welcome {current_user['full_name']}")
        print("Press 3 for Add Movie")
        print("Press 4 for Fetch All Movies")
        print("Press 5 for Find Movie by ID")
        print("Press 6 for Update Movie")
        print("Press 7 for Delete Movie")
        print("Press 8 for Add Review")
        print("Press 9 for List Reviews")
        print("Press 10 for Logout")

    print("Press 0 for Exit")

    choice = int(input("Enter your choice: "))


    if not current_user:
        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            full_name = input("Enter full name: ")
            user = User(username, password, email, full_name)
            if UserDAO.save(user):
                print(" User registered successfully")
            else:
                print(" Something went wrong")

        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = UserDAO.login(username, password)
            if user:
                current_user = user
                print(f" Login successful! Welcome {user['full_name']}")
            else:
                print(" Invalid credentials")

        elif choice == 0:
            print(" Exit")
            break

        else:
            print(" Please register or login first")

    
    else:
        if choice == 3:
            title = input("Enter movie title: ")
            genre = input("Enter genre: ")
            year = int(input("Enter year: "))
            movie = Movie(title, genre, year)
            if MovieDAO.save(movie):
                print(" Movie added successfully")
            else:
                print(" Something went wrong")

        elif choice == 4:
            MovieDAO.fetch_all()

        elif choice == 5:
            movie_id = int(input("Enter movie ID: "))
            movie = MovieDAO.find_by_id(movie_id)
            print(movie if movie else " Movie not found")

        elif choice == 6:
            movie_id = int(input("Enter movie ID: "))
            title = input("Enter new title: ")
            genre = input("Enter new genre: ")
            year = int(input("Enter new year: "))
            movie = Movie(title, genre, year)
            movie.id = movie_id
            if MovieDAO.update(movie):
                print(" Movie updated successfully")
            else:
                print(" Something went wrong")

        elif choice == 7:
            movie_id = int(input("Enter movie ID: "))
            if MovieDAO.delete(movie_id):
                print(" Movie deleted successfully")
            else:
                print(" Something went wrong")

        elif choice == 8:
            user_id = current_user["id"]
            movie_id = int(input("Enter movie ID: "))
            rating = float(input("Enter rating (0-5): "))
            comment = input("Enter comment: ")
            review = Review(user_id, movie_id, rating, comment)
            if ReviewDAO.save(review):
                print("Review added successfully")
            else:
                print(" Something went wrong")

        elif choice == 9:
            ReviewDAO.fetch_all_with_join()

        elif choice == 10:
            print(f" Logged out {current_user['full_name']}")
            current_user = None

        elif choice == 0:
            print(" Exiting...")
            break

        else:
            print(" Invalid choice")


