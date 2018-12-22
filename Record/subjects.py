import unittest

class Subjects:
    ''' This class records the subjects that are taught at school.'''

    default_subjects = ('chinese', 'math', 'english', 'science', 'politics')
    ''' These are the default subjects '''


    def __init__(self, iterable = default_subjects):
        ''' Initializes self.

        iterable -- an iterable object packing the elements
        '''

        for i in iterable:
            if type(i) != str:
                raise TypeError('Packed elements must be strings')
        self.__subjects = list(iterable)

    def get_subjects(self) -> tuple:
        return tuple(self.__subjects)

    def __iter__(self):
        return iter(self.__subjects)

    def __repr__(self):
        return repr(self.get_subjects())


def test_classes():
    a = Subjects()
    print(repr(a.get_subjects()))

if __name__ == '__main__':
    test_classes()