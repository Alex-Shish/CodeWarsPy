# Split Strings
"""Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd
number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']"""

def solution(s):
    if len(s) % 2 != 0:
        s = s + '_'
    arr = []
    i = 0
    while i < len(s):
        arr.append(s[i] + s[i + 1])
        i += 2
    return arr

print(solution("asdfadsf"))
print(solution("asdfads"))
print(solution(""))
print(solution("x"))
