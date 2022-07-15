class StringIter:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.string):
            x = self.string[self.index]
            self.index += 1
            return x
        else:
            raise StopIteration


if __name__ == '__main__':

    string_itr = StringIter("Nigeria")
    itr = iter(string_itr)

    for c in itr:
        print(c)
