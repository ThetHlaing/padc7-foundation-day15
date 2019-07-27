# Request two number inputs, hours and payrate per hours, 45 and 2.75 in this case, from the user
# Multiply the inputted number and display on the screen
# If hour exceed 40, rate will be 1.5 or normal rate for the exceeded hours
# Result should be 130.625

hour = float(input("Working hours:"))
rate = float(input("Per hour rate:"))
limit = 40

if hour > limit:
    overtime_fee = (hour-limit) * (rate * 1.5)
    salary = limit * rate
    print("Total Salary is",overtime_fee + salary)
else:
    salary = hour * rate
    print("Total Salary is",salary)