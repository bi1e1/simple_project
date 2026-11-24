from phone_search import phone, search


def test_phone():
    assert phone()['Ghala'] == 1111111111
    assert phone()['Mohammed'] == 4444444444


def test_search():
    assert search(1111111111) == 0
    assert search(4444444444) == 3
    assert search(9999999999) is None
    assert search(11111111111) is None


def main():
    test_phone()
    test_search()
    print('All tests passed')


if __name__ == '__main__':
    main()
