from art import logo

def add(n1 , n2):
    return n1+n2

def sub(n1 , n2):
    return n1-n2

def mul(n1 , n2):
    return n1*n2

def div(n1 , n2):
    return n1/n2



operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
print(logo)
choice = 'n'
while True:
    if choice == 'y':
        n1 = res
    else:
        n1 = int(input("What's the first number?:"))
    for op in operations:
        print(op)
    op_code = input("Pick an operation")
    op = operations[op_code]
    n2 = int(input("What's next number?:"))

    res = op(n1 , n2)
    print(f" {n1} {op_code} {n2} = {res}")

    choice = input(f"Type 'y' to continue calculating with {res} , or 'n' to start a new calculation:")


