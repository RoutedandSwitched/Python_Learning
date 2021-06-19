#!/usr/bin/evn python3

#Simple program to react differnt to even or odd numbers

choice = int(input("Please choose a random number between 1 and 100:"))
ans = choice % 2
if ans > 0:
    print("You picked and odd number.Fun fact, Did you know prime numbers are used in encryption")
else:
    print("You picked a stupid even number.")