class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor_one = 0
        self.cursor_two = 0
        return self

    def __next__(self):
        if self.cursor_one == len(self.list_of_list):
            raise StopIteration
        one_iter = self.list_of_list[self.cursor_one]
        two_iter = one_iter[self.cursor_two]
        self.cursor_two += 1
        if self.cursor_two == len(one_iter):
            self.cursor_two = 0
            self.cursor_one += 1
        # print(one_iter)
        return two_iter


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()