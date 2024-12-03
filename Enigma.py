'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


import random
import string

char = ' ' + string.punctuation + string.digits + string.ascii_letters
l = list(char)
e = l.copy()
random.shuffle(e)


#ENCRYPT
a = input("Enter a message: ")
b = ""

for range in a:
    i = l.index(range)
    b += e[i]
    
print(f"Your message: {a}")
print(f"Encrypted message: {b}")

    
#DECRYPT
p = input("Enter a encrypted message: ")
d = ""

for range in p:
    i = e.index(range)
    d += l[i]
    

print(f"Your encrypted message: {p}")
print(f"Decrypted message: {d}")