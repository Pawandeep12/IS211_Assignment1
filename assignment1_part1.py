def list_divide(numbers, divide=2):
    count = 0
    for number in numbers:
        if number % divide == 0:
            count += 1
    return count
class ListDivideException(Exception):
    pass
def test_list_divide():
    try:
        assert list_divide([1, 2, 3, 4, 5]) == 2
        print(list_divide([1, 2, 3, 4, 5])) #1st
        assert list_divide([2, 4, 6, 8, 10]) == 5
        print(list_divide([2, 4, 6, 8, 10])) #2nd 
        assert list_divide([30, 54, 63, 98, 100], divide=10) == 2
        print(list_divide([30, 54, 63, 98, 100], divide=10)) #3
        assert list_divide([]) == 0
        print(list_divide([])) #4
        assert list_divide([1, 2, 3, 4, 5], 1) == 5
        print( list_divide([1, 2, 3, 4, 5], 1)) #5
    except AssertionError:
        raise ListDivideException()
if __name__ == "__main__":
    test_list_divide()
    
    