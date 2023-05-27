# A number is called Automorphic number if and only if its square ends in the same digits as the number itself.
# Task
# Given a number determine if it Automorphic or not .

def automorphic(n):
    if str(n**2).endswith(str(n)):
        return "Automorphic"
    else:
        return "Not!!"
print(automorphic(n=1))
print(automorphic(n=3))
print(automorphic(n=25))
print(automorphic(n=95))
