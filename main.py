from coding_methods.ami import *
from coding_methods.m2 import *
from coding_methods.nrz import *
from coding_methods.rz import *
from upcoding.fourB_fiveB import *
from upcoding.to_hex import *
from upcoding.scrabling import *

while True:
    try:
        file = open(input("Enter filename!\n"))
        break
    except:
        print("No such File exception... Try again")

# file = open("signals", "r")


my_signals = [int(x) for x in file.read().split(" ")]
tmp = my_signals

print("Signals:")
print(*my_signals)

print("Length:", str(len(my_signals)))
C = int(input("Enter C value (MBits/s)\n"))

command = input("Enter your command or help\n")

while command != "exit":
    if command == "help":
        print("Type the command from this list:\n")
        print("nrz")
        print("manchester_diff")
        print("m2")
        print("rz")
        print("ami")
        print("exit")
        print("4b5b")
        print("restore")
        print("scrambling")
    elif command == "nrz":
        nrz(my_signals, C)
    elif command == "m2":
        manchester_two(my_signals, C)
    elif command == "rz":
        rz(my_signals, C)
    elif command == "ami":
        ami(my_signals, C)
    elif command == "4b5b":
        my_signals = fb2fb_converter(my_signals)
        nrz(my_signals, C)
    elif command == "restore":
        my_signals = tmp
    elif command == "to_hex":
        two2hex(my_signals)
    elif command == "scrambling":
        my_signals = scramble(my_signals, 5, 7)
        nrz(my_signals, C)

    command = input("Enter your command or help\n")
print("Bye!!")
