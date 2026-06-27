from day33 import add,multiply, is_palindrome, find_largest


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(10, -5) == 5


def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("python") == False


def test_find_largest():
    assert find_largest([1, 2, 3, 4, 5]) == 5
    assert find_largest([-5, -2, -10]) == -2
    assert find_largest([100]) == 100


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0