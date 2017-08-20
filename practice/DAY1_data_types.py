# Declare  variables: one of type int, one of type double, and one of type String.
# Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
# Use the  operator to perform the following operations: 
# Print the sum of  plus your int variable on a new line.
# Print the sum of  plus your double variable to a scale of one decimal place on a new line.
# Concatenate  with the string you read as input and print the result on a new line.

i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
second_int, second_double, second_string = int(input()), float(input()), str(input())
# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.
print(second_int + i)
# Print the sum of the double variables on a new line.
print(second_double + d)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + second_string)