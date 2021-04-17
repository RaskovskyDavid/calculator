from art import logo
print(logo)
#Calculator

#Add
def add(n1, n2):
    return n1+n2

#Substract
def substract(n1,n2):
    return n1-n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    if n2 == 0:
        return 0
    return n1/n2
operations = {
    "+": add,
    "-": substract,
   "*": multiply,
    "/": divide
}
bandera = 0
answer = 0
keep_going = True
while keep_going:
    if bandera == 1:
        num1 = answer
    else:
        num1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)
    operation_symbol = input("pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    keep_going_question = input("""Did you want to do more operations ?
    Type 'y' for yes and 'n' for no 
    but if you want to restar type 'r': """)
    if keep_going_question == 'n':
        keep_going= False
    if keep_going_question == 'r':
        bandera= 0
        answer = 0
        print(logo)
    else:
        bandera = 1