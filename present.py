# Define the list of fruits
fruits = ["apple", "banana", "cherry", "date"]

# Define the target element to search for
target = "banana"

# Iterate over the list of fruits
for fruit in fruits:
    # Check if the current fruit is the target
    if fruit == target:
        # Print a message if the target is found
        print("Found it!")
        # Break out of the loop since we've found the target
        break

