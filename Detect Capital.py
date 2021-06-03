def detect_capitals(word: str) -> bool:
    # create placeholder variables
    counter = 0
    capitals = 0

    # iterate through length of word
    while counter != len(word):
        # check if current character is uppercase
        if word[counter].isupper():
            # if so, increment capitals and counter by one
            capitals += 1
            counter += 1
        else:
            # if not, only increment counter by one
            counter += 1

    # if the number of capital letters is the length of the word
    # then all letters must be capital
    if counter == capitals:
        return True

    # check if only one capital
    if capitals == 1:
        # if so, check if it's the first one
        if word[0].isupper():
            # if so, return True
            return True

    # if we this point, capitals aren't being used in the right way
    return False


print(detect_capitals("USA"))
print(detect_capitals("FlaG"))
