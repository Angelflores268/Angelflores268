# ---------------------------------------------------------
# For Loop Practice
# Focus: range(), function calls, even/odd checks, countdown
#
# Rule: use functions
# Rule: test using print statements outside the function
# ---------------------------------------------------------


# Problem 1:
# Print numbers from 1 to 5.

def print_1_to_5():
    for i in range(1, 6):
        print(i)


# Problem 2:
# Print numbers from 3 to 7.

def print_3_to_7():
    for i in range(3, 8):
        print(i)


# Problem 3:
# Given n, print numbers from 1 to n.

def print_1_to_n(n):
    for i in range(1, n + 1):
        print(i)


# Problem 4:
# Given n, print numbers from 0 to n.

def print_0_to_n(n):
    for i in range(0, n + 1):
        print(i)


# Problem 5:
# Given n, print even numbers from 1 to n.

def print_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)


# Problem 6:
# Given n, print odd numbers from 1 to n.

def print_odd_numbers(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)


# Problem 7:
# Given n, count down from n to 1.

def countdown_from_n(n):
    for i in range(n, 0, -1):
        print(i)


# Problem 8:
# Print "LeetCode" 3 times.

def print_leetcode_3_times():
    for i in range(3):
        print("LeetCode")


# ---------------------------------------------------------
# Extra Range Practice
# Focus: range(start, stop, step)
# ---------------------------------------------------------


# Practice A:
# Print numbers from 1 to 7.

def print_1_to_7():
    for i in range(1, 8):
        print(i)


# Practice B:
# Print numbers from 7 down to 1.

def countdown_7_to_1():
    for i in range(7, 0, -1):
        print(i)


# Practice C:
# Print numbers from 3 to 12.

def print_3_to_12():
    for i in range(3, 13):
        print(i)


# Practice D:
# Print even numbers from 4 to 16.

def print_even_4_to_16():
    for i in range(4, 17):
        if i % 2 == 0:
            print(i)


# Practice E:
# Print numbers from 20 down to 10.

def countdown_20_to_10():
    for i in range(20, 9, -1):
        print(i)


# ---------------------------------------------------------
# Test Code
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Problem 1:")
    print_1_to_5()

    print("\nProblem 2:")
    print_3_to_7()

    print("\nProblem 3:")
    print_1_to_n(6)

    print("\nProblem 4:")
    print_0_to_n(5)

    print("\nProblem 5:")
    print_even_numbers(10)

    print("\nProblem 6:")
    print_odd_numbers(9)

    print("\nProblem 7:")
    countdown_from_n(4)

    print("\nProblem 8:")
    print_leetcode_3_times()

    print("\nPractice A:")
    print_1_to_7()

    print("\nPractice B:")
    countdown_7_to_1()

    print("\nPractice C:")
    print_3_to_12()

    print("\nPractice D:")
    print_even_4_to_16()

    print("\nPractice E:")
    countdown_20_to_10()


