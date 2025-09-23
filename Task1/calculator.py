from colorama import Fore, init

init(autoreset=True)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return  Fore.RED +"Error: Division by zero!"
    return a / b

def calculator():
    print( Fore.GREEN + "\n ---> Calculator App <---")
    while True:
        
        print(Fore.BLUE + "1. Add")
        print(Fore.BLUE + "2. Subtract")
        print(Fore.BLUE + "3. Multiply")
        print(Fore.BLUE + "4. Divide")
        print(Fore.BLUE + "5. Exit")

        choice = input(Fore.YELLOW + "Enter choice (1-5): ")

        if choice == "5":
            print(Fore.GREEN + "Exiting Calculator. Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print(Fore.RED + "Invalid choice, try again.")
            continue

        try:
            num1 = float(input(Fore.YELLOW + "Enter first number: "))
            num2 = float(input(Fore.YELLOW + "Enter second number: "))
        except ValueError:
            print(Fore.RED + "Invalid input, please enter numbers only.")
            continue

        if choice == "1":
            print(Fore.GREEN + "Result: ",add(num1, num2))
        elif choice == "2":
            print(Fore.GREEN + "Result: ",subtract(num1, num2))
        elif choice == "3":
            print(Fore.GREEN + "Result: ",multiply(num1, num2))
        elif choice == "4":
            print(Fore.GREEN + "Result: ",divide(num1, num2))

if __name__ == "__main__":
    calculator()

    