# ---------------------------------------------------------
# Return vs Print Mini Practice
# Date: 06/08/26
# Focus: returning numbers, strings, booleans, and expressions
#
# Rule: use return inside the function
# Rule: use print() outside the function to test
# Rule: do NOT hardcode example answers
# ---------------------------------------------------------


# Problem 1:
# Return the number plus 5.

def add_five(n):
    return n + 5


# Problem 2:
# Return the number times 2.

def double_number(n):
    return n * 2


# Problem 3:
# Return True if the number is even.
# Otherwise, return False.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# Problem 4:
# Return True if the number is odd.
# Otherwise, return False.

def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False


# Problem 5:
# Return "Positive" if the number is greater than 0.
# Otherwise, return "Not positive".

def positive_status(n):
    if n > 0:
        return "Positive"
    else:
        return "Not positive"


# Problem 6:
# Return the bigger of two numbers.

def bigger_number(a, b):
    if a > b:
        return a
    else:
        return b


# Problem 7:
# Return the number minus 4.

def subtract_four(n):
    return n - 4


# Problem 8:
# Return the number squared.

def square_number(n):
    return n * n


# Problem 9:
# Return True if the number is greater than 100.
# Otherwise, return False.

def greater_than_100(n):
    if n > 100:
        return True
    else:
        return False


# Problem 10:
# Return "Even" if the number is even.
# Otherwise, return "Odd".

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Problem 11:
# Return the smaller of two numbers.

def smaller_number(a, b):
    if a < b:
        return a
    else:
        return b


# ---------------------------------------------------------
# Test Code
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Problem 1:")
    print(add_five(10))             # 15

    print("\nProblem 2:")
    print(double_number(7))         # 14

    print("\nProblem 3:")
    print(is_even(6))               # True
    print(is_even(7))               # False

    print("\nProblem 4:")
    print(is_odd(5))                # True
    print(is_odd(8))                # False

    print("\nProblem 5:")
    print(positive_status(4))       # Positive
    print(positive_status(-2))      # Not positive

    print("\nProblem 6:")
    print(bigger_number(10, 4))     # 10
    print(bigger_number(3, 8))      # 8

    print("\nProblem 7:")
    print(subtract_four(10))        # 6
    print(subtract_four(7))         # 3

    print("\nProblem 8:")
    print(square_number(5))         # 25
    print(square_number(8))         # 64

    print("\nProblem 9:")
    print(greater_than_100(120))    # True
    print(greater_than_100(80))     # False

    print("\nProblem 10:")
    print(even_or_odd(6))           # Even
    print(even_or_odd(7))           # Odd

    print("\nProblem 11:")
    print(smaller_number(3, 9))     # 3
    print(smaller_number(12, 5))    # 5

