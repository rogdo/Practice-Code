## Now for something completely different:
## a string reversal program written in Python
## Ready?  1, 2, 5
def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
string = input("Enter a word or words to be reversed:  ")
print(string_reverse(string))