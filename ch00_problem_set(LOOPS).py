#22/22

# LOOPS (22pts TOTAL)
import random

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.

next = 0
i = 1
while next < 1000:
    previous = i
    i = next
    next = previous + i
    print(next, end = " ")
print("\n")


# PROBLEM 2 (Number Guessing Game - 6pts)
# Write a program that takes a random integer between 1 and 1000
# The program then asks the user to guess the number.
# After every guess, the program will say either “Lower”
# if the number it took is lower, “Higher” if the number it took is higher,
# and “You guessed it!” if the number it took is equal to the number
# It might be wise, for testing purposes, to also display the number that the
# program randomly picks, until you are sure that the program works correctly
done = False
number = random.randrange(1000)
while not done:
    user_input = int(input("Guess the number: "))
    if user_input > number:
        print("Too high!")
    if user_input < number:
        print("Too low!")
    if user_input == number:
        print("That's it! You got it!")
        done = True
print()

# PROBLEM 3 (Dice Hi-Low - 6pts)
# You roll five six-sided dice, one by one.
# How big is the probability that the value of each die
# is greater than or equal to the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.
successes = 0
for i in range(100000):
    num1 = random.randrange(1,7)
    num2 = random.randrange(1,7)
    num3 = random.randrange(1,7)
    num4 = random.randrange(1,7)
    num5 = random.randrange(1,7)

    if num1 <= num2 <= num3 <= num4 <= num5:
        successes += 1
print("Chances of success = ", successes / 100000)
print()

# Lee - Use a for loop to roll five die (DRY).  Good use of python conditional.

# PROBLEM 4 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(1,10):
                guess = int(str(d) + str(c) + str(b) + str(a))
                if guess == 4 * int(str(a) + str(b) + str(c) + str(d)):
                    print("A = ", a)
                    print("B = ", b)
                    print("C = ", c)
                    print("D = ", d)
                    quit()