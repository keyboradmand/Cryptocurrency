import random
import time

length = int(input("Input length: "))
pwd = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"~!@#$%^&*()-=,.`|'

ls = []

while True:

    while len(ls) < length:
        for i in range(length):
            ls.append(pwd[random.randint(0, len(pwd) - 1)])

    else:
        print("".join(ls))
        print("Do you like it ? [yes or no] ")
        if input() in ("no", "No", 'NO'):
            ls.clear()
            continue

        else:
            break
