import calc_art as art

# operations offered
def add(n1, n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)
num1 = int(input("What's the first number? "))

for symbol in operations:
    print(symbol)
op = input("Pick a symbol from above: ")

num2 = int(input("What's the second number? "))

answer = operations[op](num1,num2)

print(f"{num1} {op} {num2} = {answer}")