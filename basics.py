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

# --- Lists ---
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[0], fruits[-1], len(fruits))

# --- Tuples (fixed, can't change) ---
coordinates = (1, 2)

# --- Dictionaries ---
person = {"name": "Ketro", "age": 25}
print(person["name"])
person["age"] = 26

# --- Sets (unique values) ---
unique_numbers = {1, 2, 2, 3}

# --- Conditionals ---
if age >= 18:
    print("Adult")
elif age > 12:
    print("Teen")
else:
    print("Child")

# --- For loop ---
for fruit in fruits:
    print(fruit)

for i in range(5):     # 0,1,2,3,4
    print(i)

# --- While loop ---
count = 0
while count < 3:
    print("count is", count)
    count += 1

# --- Functions ---
def greet(person_name):
    return f"Hi {person_name}!"

print(greet("Class"))

# --- List comprehension (common shortcut) ---
squared_numbers = [number**2 for number in range(5)]
print(squared_numbers)

# --- Input from user ---
# user_name = input("What's your name? ")
# print(f"Nice to meet you, {user_name}")
