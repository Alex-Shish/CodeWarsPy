# Multiples of 3 or 5
# Description
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

def solution(number):
    arr = [el for el in range(number) if el % 3 == 0 or el % 5 == 0]
    return sum(arr)
print(solution(4))
print(solution(13))
print(solution(30))
