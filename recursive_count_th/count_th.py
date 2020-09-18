'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    str1 = len(word)
    str2 = len('th')

    # base case
    # if length of word is 0 or length of word is shorter than 'th'(2)
    if (str1 == 0 or str1 < str2):
        # return 0
        return 0
    # if first 2 letters in word are 'th'
    if word[0:str2] == 'th':
    # recursion
        # move word one to the right; call function; adding 1
        return count_th(word[str2 - 1:]) + 1
    # otherwise, move word one to the right; call function
    return count_th(word[str2 - 1:])
