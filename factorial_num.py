# Input from the user
num = int(input("Enter a number: "))

# Initialize factorial to 1
factorial = 1


if num < 0:                              # Check if the number is negative, zero, or positive
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
                                          # Calculate factorial using for loop
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")
