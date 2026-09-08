# 1. Basic script template
def main():
    pass

if __name__ == "__main__":
    main()


# 2. Function template
def function_name(param1, param2):
    """One-line description."""
    result = param1 + param2
    return result


# 3. Class template
class ClassName:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def method_name(self):
        return self.attr1


# 4. Input/loop template
def input_loop():
    while True:
        user_input = input("Enter something (or 'q' to quit): ")
        if user_input == 'q':
            break
        print(f"You entered: {user_input}")


# 5. Try/except template
def try_except_example():
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
    else:
        print(f"You entered {x}")


# 6. File read/write template
def file_example():
    with open("file.txt", "w") as f:
        f.write("hello")

    with open("file.txt", "r") as f:
        data = f.read()
    print(data)
