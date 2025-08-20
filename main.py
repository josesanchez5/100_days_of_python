def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2


# Dictionary mapping symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Initial input
n1 = float(input("What is your first number? "))
for symbol in operations:
    print(symbol)
op = input("Choose an operation: ")
n2 = float(input("What is your second number? "))

result = operations[op](n1, n2)
print(f"{n1} {op} {n2} = {result}")

# Loop for continued operations
while input("Do you want to continue with the result? (y/n): ").lower() == "y":
    for symbol in operations:
        print(symbol)
    op = input("Choose an operation: ")
    next_num = float(input("Enter the next number: "))
    result2 = operations[op](result, next_num)
    print(f"Result: {result} {op} {next_num} = {result2}")
