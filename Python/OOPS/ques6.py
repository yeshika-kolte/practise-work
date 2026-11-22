# 6. Movie Ticket Booking System
# Problem

# Create a movie booking system.

# Requirements

# Each movie should have:

# movie name
# total seats
# available seats
# Functionalities
# Book tickets
# Cancel tickets
# Prevent overbooking
# Display seat availability
# Concepts Practiced
# state updates
# validations
# object 

class movie:

    def __init__(self ,movie_name ,total_seats,available_seats):
        self.__movie_name = movie_name
        self.__total_seats = total_seats
        self.__available_seats = available_seats

    def book_tickets(self, num_tickets):

        if num_tickets <= self.__available_seats:
            self.__available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for {self.__movie_name}.")
        else:
            print(f"Cannot book {num_tickets} tickets. Only {self.__available_seats} seats available.")   

    def cancel_tickets(self, num_tickets):
        if self.__available_seats + num_tickets <= self.__total_seats:
            self.__available_seats += num_tickets
            print(f"{num_tickets} tickets cancelled for {self.__movie_name}.")
        else:
            print(f"Cannot cancel {num_tickets} tickets. Total seats are {self.__total_seats}.")


    def display_seat_availability(self):
        print(f"Movie: {self.__movie_name}, Available Seats: {self.__available_seats}")

m1 = movie("Inception", 100, 100)
m1.book_tickets(5)
m1.display_seat_availability()
m1.cancel_tickets(2)
m1.display_seat_availability()
     

