#!/usr/bin/env python3

##Very basic program to ask your age then tell you the year you will be 100.
name = input("Hello what is your name?")
age = int(input("How old are you?"))
year = str((2021-age)+100)
print("Thanks " + name + " In " + year + " you will be 100 years old")