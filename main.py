

# if statement:
# number = 0
#
# if number > 0:
#     print(f"Number {number} is positive")
#
# elif number == 0:
#     print(f"number is {number}")
# else:
#     print(f"Number {number} is negative")




# Multiple line of string

# name = "Michael"
# email = f"""
# Hello {name},
#
# My name is {name}, I am writting to inform you of my promotion.
#
# Thank you for your help.
#
# Kinds,
# {name}
# """
#
# print(email)

# Ternary operators:
# number = 0
# message = "Positive" if number > 0 else "Negative"
#
# print(message)


# List in python:
# print(type([]))
# numbers = [1, 2, 3, 4, 5]
#
# print(numbers.pop())
# print(numbers.append(13))
# numbers.remove(13)
# del numbers[2]
# print(numbers)


# Sets in python:
# numbers = [1, 1, 1]
#
# numberSets = {"A", "A", "B", "C"}
#
# print(numberSets)



# Union/Interception/ Difference

lettersA = {"A", "B", "C", "D"}
lettersB = {"D", "E", "F"}

# union = lettersA | lettersB
# interception = lettersA & lettersB
# difference = lettersA - lettersB
# interception.add("W")
# interce


print(f"Union = {lettersA.union(lettersB)}")
print(f"interception = {lettersA.intersection(lettersB)}")
print(f"difference = {lettersA.difference(lettersB)}")
