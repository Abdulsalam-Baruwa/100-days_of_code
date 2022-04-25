import random
test_seed = int(input("ECreate a seed number: \n"))
random.seed(test_seed)

# split string method
names_as_CSV = input("Give me everybody's names, seperated by a comma. \n")
names = names_as_CSV.split(", ")

#Get the total number of items in the list.
num_items = len(names)

#Generate a random number between 0 and the last index.
random_choice = random.randint(0, num_items - 1)

#print the corresponding name from the generated index
who_will_pay = names[random_choice]
print(who_will_pay + " is going to buy the meal today!")