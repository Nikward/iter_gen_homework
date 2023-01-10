list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
class FlatIterator:

    def __init__(self, super_list):
        self.general_list = super_list

    def __iter__(self):

        self.main_list_cursor = 0
        self.inner_list_cursor = -1
        self.current_iter = iter(self.general_list)
        return self

    def __next__(self):

        self.inner_list_cursor += 1
        if (self.inner_list_cursor) + 1 > len(self.general_list[self.main_list_cursor]):
            self.main_list_cursor += 1
            self.inner_list_cursor = 0
        if (self.main_list_cursor) + 1 > len(self.general_list):
            raise StopIteration
        return self.general_list[self.main_list_cursor][self.inner_list_cursor]

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
