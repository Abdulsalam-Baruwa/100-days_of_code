def sum_of_two_digit_number(number):
    first_digit = number[0]
    second_digit = number[1]
    sum = (int(first_digit) + int(second_digit))
    return sum


number = input("Enter a two digit number: ")

print(number[0] + " + " + number[1] + " = " + str(sum_of_two_digit_number(number)))