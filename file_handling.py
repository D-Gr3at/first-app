# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

import os

if __name__ == '__main__':
    # to open a file
    # The open() function takes two parameters; filename, and mode.
    # There are four different methods (modes) for opening a file:
    # f = open("document.txt", 'r')  # f = open("document.txt", "rt")
    # f.write('This is a test.\n')
    # f.write('We are in the United Kingdom.\n')
    # f.write('Python is great.\n')
    # f.write('''This is a test
    # How many days left
    # ON the last day''')

    # print(f.read(15))
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    #
    # for line in f:
    #     print(line)

    # f = open("files/myfile.txt", "r")
    # print(f.read())
    #
    # print(f.read(10))
    #
    # print(f.readline())
    #
    # for line in f:
    #     print(line)
    #
    os.remove('demofile.txt')
    #
    # f.close()
    #
    # if os.path.exists('document.txt'):
    #     os.remove('document.txt')
    # else:
    #     print('file not found!')
    #
    os.rmdir('files')



