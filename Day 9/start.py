programming_dictionary = {
    "bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call and call over again.",
}

#Retrieving items from a dictionary.
print(programming_dictionary["Function"])

# Adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["bug"] = "A moth in your computer"

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])