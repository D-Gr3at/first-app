# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

import re

if __name__ == '__main__':
    txt = "The rain in Spain Stains Star 20 degrees"
    x = re.search("^The.*Spain$", txt)

    print(x)

    #     findall	Returns a list containing all matches
    #     search	Returns a Match object if there is a match anywhere in the string
    #     split	Returns a list where the string has been split at each match
    #     sub	Replaces one or many matches with a string

    # findall
    all_string = re.findall('ain', txt)
    print(all_string)

    all_string = re.findall("Portugal", txt)
    print(all_string)

    # search
    x = re.search("\s", txt)
    print("The first white-space character is located in position:", x.start())

    x = re.search("Portugal", txt)
    print(x)

    # split
    x = re.split("\s", txt)
    print(x)

    x = re.split("\s", txt, 1)
    print(x)

    # The sub() function replaces the matches with the text of your choice:
    x = re.sub("S", "/", txt)
    print(x)

    x = re.sub("\s", "/", txt, 2)
    print(x)

    # A Match Object is an object containing information about the search and the result.
    # .span() returns a tuple containing the start-, and end positions of the match.
    # .string returns the string passed into the function
    # .group() returns the part of the string where there was a match

    x = re.finditer(r"\bS\w+", txt)
    # print(x.span())
    #
    # print(x.string)
    #
    # print(x.group())
    for match in x:
        print(match.group())
        print(match.string)
        print(match.span())
