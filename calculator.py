# pylint: disable=redefined-outer-name
def add(num1, num2):
    '''This function is used to add two numbers'''
    return num1 + num2

def subtract(num1, num2):
    '''This function is used to subtract two numbers'''
    return num1 - num2

def divide(num1, num2):
    '''This function is used to divide two numbers'''
    return num1 / num2

def multiply(num1, num2):
    '''This function is used to multiply two numbers'''
    return num1 * num2

if __name__ == '__main__':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Which operation to perform: ")

    result = None
    match operator:
        case '+':
            result = add(num1, num2)
        case '-':
            result = subtract(num1, num2)
        case '*':
            result = multiply(num1, num2)
        case '/':
            result = divide(num1, num2)
        case _:
            print("Invalid operator")
            exit()

    print(result)
