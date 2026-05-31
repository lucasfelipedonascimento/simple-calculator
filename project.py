def main():
    operation = input("Write the operation: Add, Subtract, Multiply, Divide: ")
    match operation:
          case "Add":
            number1 = int(input("Write the first number: "))
            number2 = int(input("Write the second number: "))
            print(f"The result of the operation is: {add(number1, number2)}")
          case "Subtract":
            number1 = int(input("Write the first number: "))
            number2 = int(input("Write the second number: "))
            print(f"The result of the operation is: {subtract(number1, number2)}")
          case "Multiply":
            number1 = int(input("Write the first number: "))
            number2 = int(input("Write the second number: "))
            print(f"The result of the operation is: {multiply(number1, number2)}")
          case "Divide":
            number1 = int(input("Write the first number: "))
            number2 = int(input("Write the second number: "))
            print(f"The result of the operation is: {divide(number1, number2)}")  

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2): 
    return number1 / number2

if __name__ == "__main__":
    main()

