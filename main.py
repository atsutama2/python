import math

def print_hi(name):
    num = 1
    flag = True
    name = "12"
    number: int = 1
    user: str = "test"
    pie = 17 / 3
    result = math.sqrt(25)

    print(f'Hi, {name}', type(name))
    print(num, type(num))
    print(flag, type(flag))
    print(int(name), type(int(name)))
    print(number, type(number))
    print(user, type(user))

    print('ほげ', 'ほげ', sep=',', end='.\n')
    print('ほげ', 'ほげ', sep=',', end='.\n')

    text = ('uuuuuuuuuuuuuuuuuuuuuuuuuuuu'
           'ffffffffffffffffffffffffffff')
    print(text)

    print('どーも\n' * 10)
    print('こんにちは.\nHow are you')
    print(r'C:\proj\name')
    print("""
        あ
    い
        う
    え
        お
    """)


    print(pie)
    print(17 // 3)
    print(5*5*5*5*5)
    print(5**5)
    print(round(pie, 2))
    print(result)

if __name__ == '__main__':
    print_hi('Hello World')
