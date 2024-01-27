class CycleIterator():
    def __init__(self, iter_list):
        self.list = iter_list
        self.len_of_list = len(iter_list)
        self.current_index = None

    def next(self):
        if self.current_index is None:
            self.current_index = 0
        else:
            self.current_index += 1
        self.current_index %= self.len_of_list
        return self.list[self.current_index]

    def prev(self):
        if self.current_index is None:
            self.current_index = -1
        else:
            self.current_index -= 1
        self.current_index %= self.len_of_list
        return self.list[self.current_index]


def test_cycle_iterator():
    a = CycleIterator([1, 2, 3])
    print(a.next())
    print(a.next())
    print(a.next())
    print(a.next())
    print(a.prev())
    print(a.prev())


if __name__ == "__main__":
    test_cycle_iterator()
