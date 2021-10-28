# Write a program which prompts the user to enter three integers separated by ","
# user input is: a, b, c; where those are numbers
# The following calculation should be displayed: a + b - c

# 10, 11, 10 = 11
# 7, 5, -1 = 13

# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
number_split = user_input.split(',')


# Convert the tokens into integers
number_tuple = []
for st in number_split:
    number_tuple.append(int(st))


# Calculate the result: a + b - c
result = number_tuple[0] + number_tuple[1] - number_tuple[2]


# Output the result
print(result)


