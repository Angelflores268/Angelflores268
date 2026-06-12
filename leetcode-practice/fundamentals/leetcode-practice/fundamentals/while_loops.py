# ---------------------------------------------------------
# While Loop Practice
# Focus: while loop setup, conditions, updating i,
# counting up, counting down, even checks, and odd checks
#
# Basic pattern:
#
# i = starting_number
# while condition:
#     print(i)
#     i = i + 1
# ---------------------------------------------------------


# Problem 1:
# Given n, print numbers from 1 to n using a while loop.

def print_1_to_n_while(n):
    i = 1

    while i <= n:
        print(i)
        i = i + 1


# Problem 2:
# Given n, print numbers from 2 to n using a while loop.

def print_2_to_n_while(n):
    i = 2

    while i <= n:
        print(i)
        i = i + 1


# Problem 3:
# Given n, print even numbers from 1 to n using a while loop.

def print_even_numbers_while(n):
    i = 1

    while i <= n:
        if i % 2 == 0:
            print(i)

        i = i + 1


# Problem 4:
# Given n, print odd numbers from 1 to n using a while loop.

def print_odd_numbers_while(n):
    i = 1

    while i <= n:
        if i % 2 != 0:
            print(i)

        i = i + 1


# Problem 5:
# Given n, count down from n to 1 using a while loop.

def countdown_from_n_while(n):
    i = n

    while i >= 1:
        print(i)
        i = i - 1


# Problem 6:
# Print numbers from 20 down to 10 using a while loop.

def countdown_20_to_10_while():
    i = 20

    while i >= 10:
        print(i)
        i = i - 1


# ---------------------------------------------------------
# Test Code
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Problem 1:")
    print_1_to_n_while(6)

    print("\nProblem 2:")
    print_2_to_n_while(6)

    print("\nProblem 3:")
    print_even_numbers_while(10)

    print("\nProblem 4:")
    print_odd_numbers_while(9)

    print("\nProblem 5:")
    countdown_from_n_while(5)

    print("\nProblem 6:")
    countdown_20_to_10_while()


