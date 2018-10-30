def duplicate_encode(word):
    returnList = []
    wordList = list(word)
    for letter in wordList:
        letter = letter.lower()
        if wordList.count(letter) == 1:
            returnList.append('(')
        else:
            returnList.append(')')
    return(''.join(returnList))