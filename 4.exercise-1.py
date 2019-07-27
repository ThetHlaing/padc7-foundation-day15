# Request two number inputs, 20 and 3.75, from the user
# Multiply the inputted number and display on the screen
# Handle the error if the input is not a number

first_number = input("First Number : ")
second_number = input("Second Number : ")
try:
    int_first_number = int(first_number)    
    int_second_number = int(second_number)
    print(int_first_number * int_second_number)
except ValueError:
    print("String received instead of an integer")
except:
    print("Unexcepted Error Occur")