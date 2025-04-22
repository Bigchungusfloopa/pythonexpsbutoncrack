def perform_division():
    
    try:
        num1 = float(input("Enter the desired number:"))
        num2 = float(input("Enter the desired number:"))

        result = num1/num2
        print(f"Result of the above division is {result}")

    except ZeroDivisionError:
        print("Error,Can't divide by zero")
    except ValueError:
        print("Error, Invalid value")
    except Exception as e:
        print(f"An unexpected error occured:{e}") 

perform_division()                  
