import art
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def mod(n1, n2):
    return n1 % n2
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "%": mod,
}
def calculator():
    print(art.logo)
    should_run = True
    num1 = float(input("Enter the first number: "))
    while should_run:
        for key in operations:
            print(key)
        op=input("Enter the operation: ")
        num2 = float(input("Enter the second number: "))
        answer = operations[op](num1, num2)
        print(f"{num1} {op} {num2} = {answer}")
        choice=input(f"Type 'y' to continue calculating with {answer},or 'n' to start a new calculation: ")
        if choice=="y":
            num1=answer
        else:
            should_run = False
            print("\n"*100)
            calculator()
calculator()
