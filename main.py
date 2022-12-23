from calculator import add


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


# print(f"Union = {lettersA.union(lettersB)}")
# print(f"interception = {lettersA.intersection(lettersB)}")
# print(f"difference = {lettersA.difference(lettersB)}")


# Python dictionary:
# person = {"name": " Joyce", "age": 35, "address": "Lagos, Nigeria"}
# person["name"] = "Joyce"
# print(person["name"])

# for loop through LIST and SETs in python:
# names = ["Olatomiwa", "Ikeoluwa", "Simisoluwa", "Oluwasikemi"]
#
# cars = { "Benz", "Toyota", "Jeep"}
#
# for name in names:
#     print(name)

# for car in cars:
#     print(car)

# Looping through dictionary in python:

# person = {
#     "name": "Michael",
#     "age": 25,
#     "location": "Lagos"
# }
#
# for key, value in person.items():
#     print(f"value: {value}")
#     print(f"key: {key}")


# Exercise:
# loop through a list of numbers and sum the value:
# numbers = [1, 2, 3, 4]
#
# number_sum = 0
# for number in numbers:
#     number_sum += number

# print(number_sum)

# car = {
#     "brand": "Toyota",
#     "year_of_produce": 2022,
# }

# for key, value in car.items():
#     print(value)


# While loop in python:
# number = 0
#
# while number < 10:
#     print(number + 1)
#     number += 1

# def say_hello(name):
#     print(f"Hello {name}")
#
# say_hello("Simi")

# function that return if you are adult:

# def check_age(age):
#     if age > 18:
#         print("You are an adult")
#     else:
#         print("You are not elegable yet")
# check_age(19)

# from math import ceil
#
# print(ceil(2.3445))

# print(add(2, 3))

# python class declaration:
class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
    def drive(self, speed):
        print(f"{self.brand} is moving on {speed}/kmph")


toyota = Car("Toyota", "Blue", 2008)
benz = Car("Benz", "Green", 2008)
jeep = Car("Jeep", "Blue", 2008)
#
# toyota.drive(200)
# benz.drive(300)
# jeep.drive(150)




class Person:
    def __init__(self, name, sex, age, height):
        self.sex = sex
        self.name = name
        self.age = age
        self.height = height
    def speak(self, language):
        print(f"Says hello in {language}")

    def say_hello(self):
        print(f"Hello {self.name}, how are you today")

    def is_adult(self):
        if self.age >= 18:
            print("You are an adult")



# lady = Person("Moji", "female", 23, 3.67)
# lady.say_hello()
# lady.is_adult()



class Airplane:

    def __init__(self, brand, fleat_number, number_seats):
        self.brand = brand
        self.fleat_number = fleat_number
        self.number_seats = number_seats

    def fly(self):
        print(f"{self.fleat_number} is flying")


boan_323 = Airplane("boan_323", "F323", 34)
boan_323.fly()