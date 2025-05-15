#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

print(happy_new_year())

def square_integers(int_list):
    return [int_list ** 2 for int_list in int_list]

print(square_integers([1, 2, 3, 4]))
print(square_integers([-2, 0, 5]))

def fizzbuzz():
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

print(fizzbuzz())



