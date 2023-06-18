from main.utils import arrs


def testing_get():
    assert arrs.get([1, 2, 3], 0, "test") == 1
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([1, 2, 3], -10, "test") == "test"
    assert arrs.get([], -1, "test") == "test"
    assert arrs.get([1, 2, 3], 4, "gtyu") == "gtyu"





def testing_slice():
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice([1, 2, 3, 4], -1, 3) == []
    assert arrs.my_slice([1, 2, 3, 4], -5, 3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]