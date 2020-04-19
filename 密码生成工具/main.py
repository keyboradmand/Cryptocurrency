import random

length = int(input("Input length: "))
pwd = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"~!@#$%^&*()-=,.`|'

ls = []

while len(ls) < length:
    for i in range(length):
        ls.append(pwd[random.randint(0, len(pwd) - 1)])


print("".join(ls))
