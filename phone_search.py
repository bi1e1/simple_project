def main():
    while True:
        try:
            while True:
                number = int(input('Just put the number and you will get the name AUTO ::: '))
                if len(str(number)) == 10:
                    break
                else:
                    print('!!!! we accept only 10 digits !!!!')
            get_name(number)
        except ValueError:
            print('!!!! We accept only numbers !!!!')

def phone():
    numbers = {
        'Ghala' : 1111111111,
        'Ahmed' : 2222222222,
        'Ali' : 3333333333,
        'Mohammed' : 4444444444
    }
    return numbers

def search(number):
    x = phone()
    y = list(x.values())
    for a in y :
        if number == a :
            key = y.index(a)
            return key
    return None

def get_name(number):
    x = phone()
    j = list(x.keys())
    key = search(number)
    if key is None:
        print('Number not found')
    else:
        print(f'{number} of {j[key]}')

if __name__ == "__main__":
    main()
