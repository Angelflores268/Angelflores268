# ---------------------------------------------------------
# Python Conditional Practice
# Focus: functions, parameters, return values, if/else,
# comparison operators, and Boolean logic
#
# Rule: use return inside the function
# Rule: use print() outside the function to test
# Rule: do NOT hardcode example answers
# ---------------------------------------------------------


# Problem 1:
# Return True if the score is between 0 and 100.
# Otherwise, return False.

def is_valid_score(score):
    return score >= 0 and score <= 100


# Problem 2:
# Return True if someone is eligible for a discount.
# A person gets a discount if they are 12 or younger OR 65 or older.

def is_discount_eligible(age):
    return age <= 12 or age >= 65


# Problem 3:
# Return True if someone can drive.
# A person can drive if they are 18 or older,
# OR if they are at least 16 and have a permit.

def can_drive(age, has_permit):
    return age >= 18 or (age >= 16 and has_permit)


# Problem 4:
# Return True if someone can enter a movie.
# A person can enter if they are at least 13 and have a ticket.

def can_enter_movie(age, has_ticket):
    return age >= 13 and has_ticket


# Problem 5:
# Return True if someone can access the gym.
# A person can access the gym if they are at least 18
# and they either have a membership or are a guest.

def can_access_gym(age, has_membership, is_guest):
    return age >= 18 and (has_membership or is_guest)


# Problem 6:
# Return True if a student can submit an assignment.
# A student can submit if they are logged in, have a file,
# and the file size is 25 MB or less.

def can_submit_assignment(is_logged_in, has_file, file_size):
    return is_logged_in and has_file and file_size <= 25


# Problem 7:
# Return True if a customer gets free shipping.
# A customer gets free shipping if their total is $50 or more
# OR if they are a member.

def can_get_free_shipping(total, is_member):
    return total >= 50 or is_member


# Problem 8:
# Return True if a user can log in.
# A user can log in if they have an account and are not banned.

def can_login(has_account, is_banned):
    return has_account and not is_banned


# ---------------------------------------------------------
# Return vs Print Mini Practice
# Date: 06/08/26
# ---------------------------------------------------------


# Return the number plus 5.

def add_five(n):
    return n + 5


# Return the number times 2.

def double_number(n):
    return n * 2


# Return True if the number is even.
# Otherwise, return False.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# Return True if the number is odd.
# Otherwise, return False.

def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False


# Return "Positive" if the number is greater than 0.
# Otherwise, return "Not positive".

def positive_status(n):
    if n > 0:
        return "Positive"
    else:
        return "Not positive"


# Return the bigger of two numbers.

def bigger_number(a, b):
    if a > b:
        return a
    else:
        return b


# Return the number minus 4.

def subtract_four(n):
    return n - 4


# Return the number squared.

def square_number(n):
    return n * n


# Return True if the number is greater than 100.
# Otherwise, return False.

def greater_than_100(n):
    if n > 100:
        return True
    else:
        return False


# Return "Even" if the number is even.
# Otherwise, return "Odd".

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Return the smaller of two numbers.

def smaller_number(a, b):
    if a < b:
        return a
    else:
        return b


# ---------------------------------------------------------
# Test Code
# This only runs when you run this file directly.
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Problem 1:")
    print(is_valid_score(85))     # True
    print(is_valid_score(120))    # False

    print("\nProblem 2:")
    print(is_discount_eligible(10))   # True
    print(is_discount_eligible(30))   # False
    print(is_discount_eligible(70))   # True

    print("\nProblem 3:")
    print(can_drive(18, False))   # True
    print(can_drive(16, True))    # True
    print(can_drive(16, False))   # False

    print("\nProblem 4:")
    print(can_enter_movie(13, True))   # True
    print(can_enter_movie(12, True))   # False
    print(can_enter_movie(15, False))  # False

    print("\nProblem 5:")
    print(can_access_gym(20, True, False))   # True
    print(can_access_gym(20, False, True))   # True
    print(can_access_gym(16, True, False))   # False

    print("\nProblem 6:")
    print(can_submit_assignment(True, True, 20))    # True
    print(can_submit_assignment(True, True, 30))    # False
    print(can_submit_assignment(False, True, 10))   # False

    print("\nProblem 7:")
    print(can_get_free_shipping(60, False))   # True
    print(can_get_free_shipping(20, True))    # True
    print(can_get_free_shipping(20, False))   # False

    print("\nProblem 8:")
    print(can_login(True, False))   # True
    print(can_login(True, True))    # False
    print(can_login(False, False))  # False

    print("\nReturn vs Print Practice:")

    print(add_five(10))             # 15
    print(double_number(7))         # 14
    print(is_even(6))               # True
    print(is_even(7))               # False
    print(is_odd(5))                # True
    print(is_odd(8))                # False
    print(positive_status(4))       # Positive
    print(positive_status(-2))      # Not positive
    print(bigger_number(10, 4))     # 10
    print(bigger_number(3, 8))      # 8
    print(subtract_four(10))        # 6
    print(subtract_four(7))         # 3
    print(square_number(5))         # 25
    print(square_number(8))         # 64
    print(greater_than_100(120))    # True
    print(greater_than_100(80))     # False
    print(even_or_odd(6))           # Even
    print(even_or_odd(7))           # Odd
    print(smaller_number(3, 9))     # 3
    print(smaller_number(12, 5))    # 5

