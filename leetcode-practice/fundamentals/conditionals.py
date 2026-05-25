# Python Conditional Practice Problems
# Completed: 8 problems
# Topic: if/else, return vs print, comparisons, and/or/not, Boolean variables


# 1. is_valid_score(score)
# Description:
# Return True if the score is valid.
# A valid score is from 0 to 100, including both 0 and 100.
def is_valid_score(score):
    if score >= 0 and score <= 100:
        return True
    else:
        return False


# 2. is_discount_eligible(age)
# Description:
# Return True if a person gets a discount.
# A person gets a discount if they are 12 or younger OR 65 or older.
def is_discount_eligible(age):
    if age <= 12 or age >= 65:
        return True
    else:
        return False


# 3. can_drive(age, has_permit)
# Description:
# Return True if the person can drive.
# A person can drive if they are 18 or older,
# OR if they are 16 or older and have a permit.
def can_drive(age, has_permit):
    if age >= 18:
        return True
    elif age >= 16 and has_permit:
        return True
    else:
        return False


# 4. can_enter_movie(age, has_ticket)
# Description:
# Return True if the person can enter the movie.
# A person can enter if they are 13 or older AND have a ticket.
def can_enter_movie(age, has_ticket):
    if age >= 13 and has_ticket:
        return True
    else:
        return False


# 5. can_access_gym(age, has_membership, is_guest)
# Description:
# Return True if the person can access the gym.
# A person can enter if they are 18 or older and have a membership,
# OR if they are marked as a guest.
def can_access_gym(age, has_membership, is_guest):
    if (age >= 18 and has_membership) or is_guest:
        return True
    else:
        return False


# 6. can_submit_assignment(is_logged_in, has_file, file_size)
# Description:
# Return True if the student can submit the assignment.
# A student can submit if they are logged in,
# have a file, and the file size is 10 or less.
def can_submit_assignment(is_logged_in, has_file, file_size):
    if is_logged_in and has_file and file_size <= 10:
        return True
    else:
        return False


# 7. can_get_free_shipping(total, is_member)
# Description:
# Return True if the customer gets free shipping.
# A customer gets free shipping if their total is 50 or more,
# OR if they are a member.
def can_get_free_shipping(total, is_member):
    if total >= 50 or is_member:
        return True
    else:
        return False


# 8. can_login(has_account, is_banned)
# Description:
# Return True if the user can log in.
# A user can log in if they have an account AND they are not banned.
def can_login(has_account, is_banned):
    if has_account and not is_banned:
        return True
    else:
        return False


# Test cases

print("1. is_valid_score")
print(is_valid_score(95))    # True
print(is_valid_score(0))     # True
print(is_valid_score(100))   # True
print(is_valid_score(-3))    # False
print(is_valid_score(120))   # False

print("\n2. is_discount_eligible")
print(is_discount_eligible(10))  # True
print(is_discount_eligible(12))  # True
print(is_discount_eligible(13))  # False
print(is_discount_eligible(64))  # False
print(is_discount_eligible(65))  # True

print("\n3. can_drive")
print(can_drive(18, False))  # True
print(can_drive(16, True))   # True
print(can_drive(16, False))  # False
print(can_drive(15, True))   # False
print(can_drive(20, False))  # True

print("\n4. can_enter_movie")
print(can_enter_movie(13, True))   # True
print(can_enter_movie(12, True))   # False
print(can_enter_movie(15, False))  # False
print(can_enter_movie(20, True))   # True

print("\n5. can_access_gym")
print(can_access_gym(20, True, False))   # True
print(can_access_gym(20, False, False))  # False
print(can_access_gym(16, True, False))   # False
print(can_access_gym(16, False, True))   # True
print(can_access_gym(30, False, True))   # True

print("\n6. can_submit_assignment")
print(can_submit_assignment(True, True, 5))    # True
print(can_submit_assignment(True, True, 10))   # True
print(can_submit_assignment(True, True, 12))   # False
print(can_submit_assignment(True, False, 5))   # False
print(can_submit_assignment(False, True, 5))   # False

print("\n7. can_get_free_shipping")
print(can_get_free_shipping(50, False))  # True
print(can_get_free_shipping(49, False))  # False
print(can_get_free_shipping(20, True))   # True
print(can_get_free_shipping(80, True))   # True

print("\n8. can_login")
print(can_login(True, False))   # True
print(can_login(True, True))    # False
print(can_login(False, False))  # False
print(can_login(False, True))   # False
