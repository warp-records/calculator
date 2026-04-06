
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print(mul(5, add(5, 10)))
print(div(100, 10))

def tui():
    print("Simple TUI Calculator")
    print("=====================")
    print("1. Add")
    print("2. Multiply")
    print("3. Divide")
    print("4. Exit")

    while True:
        try:
            choice = input("\nEnter choice (1-4): ")

            if choice == '4':
                print("Goodbye!")
                break
            elif choice in ['1', '2', '3']:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == '1':
                    result = add(a, b)
                    print(f"Result: {a} + {b} = {result}")
                elif choice == '2':
                    result = mul(a, b)
                    print(f"Result: {a} * {b} = {result}")
                elif choice == '3':
                    if b == 0:
                        print("Error: Cannot divide by zero")
                    else:
                        result = div(a, b)
                        print(f"Result: {a} / {b} = {result}")
            else:
                print("Invalid choice. Please enter 1-4.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

# Run the TUI
tui()
