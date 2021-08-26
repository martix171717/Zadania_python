def palindrome(word):
    '''
    Checks if passed argument is a palindrome i.e. a word, number or phrase,
    which reads the same backward as forward, such as madam or abba.
    If passed argument is a palindorme, returns Boolean value True.
    Else, returns Boolean value False.
    Arguments:
    word
    '''
    if list(word) == list(reversed(word)):
        return True
    elif list(word) != list(reversed(word)):
        return False
    
print(palindrome("abba"))