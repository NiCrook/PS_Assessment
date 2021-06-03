def same_string_check(s: str, t: str) -> bool:
    """
    Given two input variables, string: 's' and string: 't', remove any backspaces, '#', and the character before,
    then compare if 's' == 't'.
    :param s: string more than one character and less than two-hundred characters in length
    :param t: string more than one character and less than two-hundred characters in length
    :return: if 's' == 't', return True, else, return False
    """

    # Checking the length of the input variables
    if len(s) < 1 or len(s) > 200:
        return False
    if len(t) < 1 or len(t) > 200:
        return False

    def backspace(word: str) -> str:
        """
        Nested function to check for backspaces, '#', in variable string: "word", and removes them
        and the character before, if there is one.
        :param word: string
        :return: backspaced string
        """
        for char in word:
            if char == '#':
                ind = word.index('#')
                if ind == 0:
                    word = word[ind+1:]
                else:
                    word = word[:ind-1] + word[ind+1:]
        return word

    # Compare backspaced 's' and backspaced 't'
    if backspace(s) == backspace(t):
        return True
    else:
        return False


print(same_string_check("ab#c", "ad#c"))
print(same_string_check("ab##", "c#d#"))
print(same_string_check("a##c", "#a#c"))
print(same_string_check("a#c", "b"))
