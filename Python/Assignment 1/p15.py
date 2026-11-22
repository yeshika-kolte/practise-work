# 15. Write a python program to accept the cost price of a bike
#     and display the road tax to be paid according to the 
#     following criteria.
#     Cost Price(In Rs)		     Tax
#      > 100000			         15 %
#      >50000 and <=100000	     10 %
#      <=50000			         5%

cost = int(input("Enter cost price (in Rs): "))
if cost > 100000:
    tax = 15
elif cost > 50000 and cost<=100000:
    tax = 10
else:
    tax = 5
amt = cost * (tax / 100)
print("Tax to pay :", (amt))

