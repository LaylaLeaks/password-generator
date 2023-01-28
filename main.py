import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

all = lower + upper + numbers + symbols
lenght = 16
passwort = "".join(random.sample(all,lenght))

print(passwort)

'''
If you have any issues please message me on Discord or Twitter and I will respond as quickly as possible!
Twitter: @RealSaii_
Discord: Saiiofficial#7453
'''