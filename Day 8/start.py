# Review:
# Create a function called greet().
def greet():

# Write 3 print statements inside the function.
    print("Hello World!")
    print("You're welcome!")
    print("The third print statement.")
# Call the greet() function and run your code.
greet()

# Function with Input
def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How do you do, {name}?")

greet_with_name("Angela")

# Function with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is the weather like in {location}?")

greet_with("Jack Bauer", "Kansas")

# Functions with keyword arguments
greet_with(name="Angela", location="London")