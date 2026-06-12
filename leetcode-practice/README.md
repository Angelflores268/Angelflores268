# LeetCode Practice

## Current Progress

This repository tracks my Python practice before moving into full LeetCode problems.

The goal is to build a strong foundation in Python basics, including conditionals, Boolean logic, loops, functions, return values, accumulators, lists, strings, and beginner LeetCode patterns.

I am using this repo to document my progress, practice problems, mistakes, and notes as I build up my coding interview skills step by step.

---

## Topics Covered

- Functions with parameters
- `return` vs `print`
- `if` / `else`
- Comparison operators: `>=`, `<=`, `==`, `!=`, `>`, `<`
- Boolean logic: `and`, `or`, `not`
- Boolean variables such as `has_ticket`, `is_member`, and `is_banned`
- `for` loops
- `while` loops
- `range(start, stop)`
- `range(start, stop, step)`
- Even and odd number checks
- Countdown loops
- Testing Python functions in VS Code using `print()`

---

## Problems Completed

### Conditional Practice

1. `is_valid_score(score)`  
   Checks whether a score is between 0 and 100.

2. `is_discount_eligible(age)`  
   Uses `or` logic to check if someone is 12 or younger or 65 or older.

3. `can_drive(age, has_permit)`  
   Uses mixed conditions to check if someone can drive based on age and permit status.

4. `can_enter_movie(age, has_ticket)`  
   Uses `and` logic to check if someone is old enough and has a ticket.

5. `can_access_gym(age, has_membership, is_guest)`  
   Mixes `and` and `or` logic to check gym access.

6. `can_submit_assignment(is_logged_in, has_file, file_size)`  
   Uses multiple `and` conditions to check if a student can submit an assignment.

7. `can_get_free_shipping(total, is_member)`  
   Uses `or` logic to check if a customer gets free shipping.

8. `can_login(has_account, is_banned)`  
   Uses `not` to check if a user is not banned.

---

## Practice Log

### 05/23/26 — First LeetCode-Style Python Practice

This was my first LeetCode-style Python practice session. The focus was reviewing basic Python before getting deeper into conditionals.

**Problem Practiced:**

- `can_enter_movie(age, has_ticket)`

**Skills Practiced:**

- Functions
- Parameters
- Conditionals
- Boolean values
- `return True`
- `return False`

---

### 05/28/26 — Loop Practice Set 3

This session focused on basic `for` loops and `range()`.

**Problems Practiced:**

- Print numbers from 1 to 5
- Print numbers from 3 to 7
- Print numbers from 1 to `n`
- Print numbers from 0 to `n`
- Print even numbers from 1 to `n`
- Print odd numbers from 1 to `n`
- Countdown from `n` to 1
- Print `"LeetCode"` 3 times

**Skills Practiced:**

- `for` loops
- `range(start, stop)`
- `range(start, stop, step)`
- Function calls
- Even checks
- Odd checks
- Countdown loops

---

### 05/29/26 — Functions, Parameters, Return Values, and If Statements

This session focused on Python fundamentals needed before LeetCode.

The main goal was understanding how functions work, how parameters work, how `return` works, and how to test functions using `print()` outside the function.

**Problems Practiced:**

- Return the same number
- Add one
- Subtract one
- Double number
- Square number
- Is positive
- Is even
- Pass or fail
- Age status
- Bigger number
- Between 1 and 10

**Skills Practiced:**

- Functions
- Parameters
- Return values
- `print()` vs `return`
- If statements
- Comparison operators
- Boolean logic
- Avoiding hardcoded answers

---

### 05/29/26 — Range Practice

This was extra practice with `range(start, stop, step)`.

**Problems Practiced:**

- Print numbers from 1 to 7
- Countdown from 7 to 1
- Print numbers from 3 to 12
- Print even numbers from 4 to 16
- Countdown from 20 to 10

**Skills Practiced:**

- `range(start, stop, step)`
- Positive step
- Negative step
- Counting upward
- Counting downward
- Even number checks

---

### 06/01/26 — For Loop Review and Range Logic

This session focused on understanding `for i in range()` more deeply.

**Key Concepts:**

- `n` is the ending number.
- `i` is the current number the loop is checking.
- `n` stays the same.
- `i` changes every loop.
- `range(1, n + 1)` goes from 1 to `n`.
- Python stops before the stop number.

**Skills Practiced:**

- `range(1, n + 1)`
- `i` vs `n`
- Even checks
- Odd checks
- Avoiding hardcoding

---

### 06/01/26 — While Loop Intro

This session introduced basic `while` loops.

**Problems Practiced:**

- Print numbers from 1 to `n` using a while loop
- Print numbers from 2 to `n` using a while loop

**Key Concept:**

A `for` loop handles counting automatically. A `while` loop makes me control the counting myself.

Basic pattern:

```python
i = 1
while i <= n:
    print(i)
    i = i + 1