# Description:
# The goal of this exercise is to convert a string to a new string where each character in the new string is "("
# if that character appears only once in the original string, or ")" if that character appears more than once in
# the original string. Ignore capitalization when determining if a character is a duplicate.
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

def duplicate_encode(word):
    w = word.lower()
    str = ''
    lst = {}
    for i in w:
        lst[i] = lst.get(i, 0) + 1
    for i in w:
        if lst[i] > 1:
            str += ")"
        else:
            str += "("
    return str

print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))