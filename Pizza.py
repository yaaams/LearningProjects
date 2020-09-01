#radius of pizza as it pertains to area
#I suspect there is an easier where to write this by using classes

pi = 3.14159
#Pizza 1
pizza1 = float(input("What is the diameter of the first pizza in inches? "))
pizza1_cost = float(input("What is the price of the first pizza? "))
pizza1_area = ((pizza1/2)**2) * pi
pizza_ratio1 = pizza1_cost/ pizza1_area

#Pizza 2
pizza2 = float(input("What is the diameter of the second pizza? "))
pizza2_cost = float(input("What is the price of the second pizza? "))
pizza2_area = ((pizza2/2)**2) * pi
pizza_ratio2 = pizza2_cost/ pizza2_area


print(f"The first pizza is {round(pizza_ratio1, 3)} cents per sq. inch, while the second is {round(pizza_ratio2, 3)} cents per sq. inch.")
if pizza_ratio1 > pizza_ratio2:
   print("The second pizza is a better value." )
elif pizza_ratio1 < pizza_ratio2:
    print("The first pizza is a better value")
else:
    print("\nThe pizzas have the same value.")


print("\nDone with pizza value calculations")