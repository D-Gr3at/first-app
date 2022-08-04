# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

import re

if __name__ == '__main__':
    txt = "The rain in Spain"
    x = re.search("^The.*Spain$", txt)

    # print(x)

    #     findall	Returns a list containing all matches
    #     search	Returns a Match object if there is a match anywhere in the string
    #     split	Returns a list where the string has been split at each match
    #     sub	Replaces one or many matches with a string

    # findall
    # all_string = re.findall('ain', txt)
    # print(all_string)
    #
    # all_string = re.findall("Portugal", txt)
    # print(all_string)

    # search
    # x = re.search("\s", txt)
    # print("The first white-space character is located in position:", x.start())
    #
    # x = re.search("Portugal", txt)
    # print(x)

    # split
    x = re.split("\s", txt)
    print(x)

    x = re.split("\s", txt, 1)
    print(x)
