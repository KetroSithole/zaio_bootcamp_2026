
"""
Python Basics Practice Template
Fill in your answers below each question. Run the file to check your output.
"""

# =========================================================
# --- Reference code (from the original example) ---
# =========================================================

# --- Print ---
print("Hello, world!")

# --- Variables & data types ---
name = "Ketro"        # str
age = 25              # int
height = 1.8          # float
is_student = True     # bool

# --- Basic math operators ---
first_number = 10
second_number = 3
print(
    first_number + second_number,
    first_number - second_number,
    first_number * second_number,
    first_number / second_number,
    first_number % second_number,
    first_number ** second_number,
    first_number // second_number,
)

# --- String basics ---
greeting = "Hello" + " " + name   # concatenation
print(f"{greeting}, you are {age} years old")  # f-string
print(name.upper(), name.lower(), len(name))


# =========================================================
# SECTION 1: Print & Basics
# =========================================================

# Q1: Write a line of code that prints your own name using print().


# Q2: What will print("Hello", "world") output — does it add a space
#     automatically? Try it below.


# Q3: What happens if you try to run print(Hello, world!) without quotes?
#     Why? (Try it, then write your explanation as a comment.)
# Your answer:


# =========================================================
# SECTION 2: Variables & Data Types
# =========================================================

# Q4: Create a variable `city` and assign it your city as a string.
#     What data type is it?


# Q5: What's the difference between age = 25 and age = "25"?
# Your answer:


# Q6: Use type() to check the data type of `height`. What does it return?


# Q7: Change is_student to False and print it. What data type is True/False?


# Q8: Create a float variable called `price` with the value 19.99.


# Q9: What would happen if you wrote age = 25 then age = "twenty five" —
#     can a variable change type? Try it and explain.
# Your answer:


# =========================================================
# SECTION 3: Math Operators
# =========================================================

# Q10: Without running the code, predict the output of
#      first_number % second_number. What does % actually do?
# Your prediction:


# Q11: What's the difference between / and // in Python?
#      Predict both results for 10 / 3 and 10 // 3, then check.
# Your prediction:


# Q12: What does first_number ** second_number calculate?
#      (Hint: it's not multiplication)
# Your answer:


# Q13: Swap the values of first_number and second_number — how do the
#      results of - and / change?


# Q14: Write an expression using second_number that calculates its square.


# Q15: If first_number = 7 and second_number = 2, what would
#      first_number % second_number return, and why?
# Your answer:


# =========================================================
# SECTION 4: Strings
# =========================================================

# Q16: What does the + operator do when used between two strings,
#      compared to two numbers?
# Your answer:


# Q17: Rewrite the f-string below using string concatenation (+)
#      instead of an f-string.
# f"{greeting}, you are {age} years old"


# Q18: What does len(name) count — letters only, or does it include
#      spaces/symbols too? Test it with a name that has a space.


# Q19: What would name.upper() and name.lower() do if
#      name = "Ketro Sithole" (with a space)? Try it.


# Q20: Try name[0] — what do you think this returns?
#      (Hint: think about indexing)