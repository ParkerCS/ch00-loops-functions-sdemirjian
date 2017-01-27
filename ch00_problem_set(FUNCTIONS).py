#SECTION 2 - FUNCTIONS (20PTS TOTAL)
import math
import random

#PROBLEM 1 (Length of String - 3pts)
# Make a function which asks the user to enter a string, then prints the length of that string.
# You will need to use the input() function.
# Make a call to that function
def print_string(user_input):
    print(len(user_input))

user_input = input("Say something: ")
print_string(user_input)


# PROBLEM 2 (Pythagorean theorem - 4pts)
# The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths
# of the other two sides (or a^2 + b^2 = c^2).
# Write a program that asks the user for the lengths of the two sides that meet at a right angle.
# Then calculate the length of the third side, and display it in a nicely formatted way.
# You may ignore the fact that the user can enter negative or zero lengths for the sides.
def pythag(a,b):
    print("The length of the third side is: ", (a**2 + b**2)**(1/2))

pythag(float(input("What is the length of the first side? ")), float(input("What is the length of the second side? ")))

# PROBLEM 3 (Biggest, smallest, average - 4pts)
# Make a function to ask the user to enter three numbers.
# Then print the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
# Make a call to your function.
def big_small_average(a,b,c):
    if a > b and a > c:
        print(a, "is the biggest number")
    if b > a and b > c:
        print(b, "is the biggest number")
    if c > a and c > b:
        print(c, "is the biggest number")

    if a < b and a < c:
        print(a, "is the smallest number")
    if b < a and b < c:
        print(b, "is the smallest number")
    if c < a and c < b:
        print(c, "is the smallest number")

    if a == b and a == c:
        print("There is no smallest! They are all ", a)

    print("The average of the three numbers is: ", round((a + b + c)/3))

big_small_average(int(input("What is the first number? ")), int(input("What is the second number? ")), int(input("What is the third number? ")))


# PROBLEM 4 (e to the... - 3pts)
# Calculate the value of e (from the math library) to the power of -1, 0, 1, 2, and 3.
# display the results, with 5 decimals, in a nicely formatted manner.
def powers_of_e():
    print("e to the power of -1 = ", round(math.e**(-1),5))
    print("e to the power of 0 = ", round(math.e**0,5))
    print("e to the power of 1 = ", round(math.e**1,5))
    print("e to the power of 2 = ", round(math.e**2,5))
    print("e to the power of 3 = ", round(math.e**3,5))

powers_of_e()

# PROBLEM 5 (Random int - 3pts)
# Generate a random integer between 1 and 10 (1 and 10 both included),
# but only use the random() function (randrange is not allowed here)
bloop = round(random.random(),1) * 10
print(bloop)

# PROBLEM 6 (add me, multiply me - 3pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.
def add_product(a,b):
    sum = a + b
    product = a * b
    return sum, product
