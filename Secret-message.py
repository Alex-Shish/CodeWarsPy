# Secret Message
"""There is a secret message in the first six sentences of this kata description. Have you ever felt like there was
something more being said? Was it hard to figure out that unspoken meaning? Never again! Never will a secret
go undiscovered. Find all duplicates from our message!
Your job is to write a function that will find the secret words of the message and return them in order. The words
in the secret message should be ordered in the order in which they are found as a duplicate, for example:

'This is a test. this test is fun.' # --> 'this test is'
Notes
The input will always be a string.
If the random tests repeat a word multiple times, it should show up in the secret message only once, based on
the position of the first time it was duplicated.
The punctuation and casing of words (uppercase, lowercase) should not matter for the purpose of this kata.
We are only concerned with word duplication."""

def find_secret_message(paragraph):
    s = paragraph.lower()
    # marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
    marks = '''!;,.'''
    for x in s:
        if x in marks:
            s = s.replace(x, "")
    s = s.replace("  ", " ")
    a = s.split(" ")
    r = []
    for el in a:
        if a.count(el) > 1:
            r.append(el)
    r2 = []
    for i in range(int(len(r) / 2), int(len(r))):
        r2.append(r[i])
    return " ".join(r2)

print(find_secret_message('This is a test. this test is fun.'))
print(find_secret_message('asdf qwer zxcv. zxcv fdsa rewq. qazw asdf sxed. qwer crfv.'))
print(find_secret_message('sky codewars! secret have sun talks bad, the? bad wants! eats out? bad, have? eats codewars never. moon sky code! a, chocolate: saves. sleeps good: kills good. is. pippi'))