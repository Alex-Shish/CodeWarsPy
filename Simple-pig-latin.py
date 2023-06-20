# Simple Pig Latin
# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    arr = text.split()
    arr_new = []
    for el in arr:
        if el.isalpha():
            arr_new.append(el.replace(el[0], '', 1) + el[0] + 'ay')
        else:
            arr_new.append(el)
    return " ".join(arr_new)

print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))
print(pig_it('Hello world !'))
