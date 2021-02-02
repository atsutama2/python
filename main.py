# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    num = 1
    flag = True
    name = "12"
    number: int = 1
    user: str = "test"

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}', type(name))  # Press ⌘F8 to toggle the breakpoint.
    print(num, type(num))
    print(flag, type(flag))
    print(int(name), type(int(name)))
    print(number, type(number))
    print(user, type(user))

    print('ほげ', 'ほげ', sep=',', end='.\n')
    print('ほげ', 'ほげ', sep=',', end='.\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hello World')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
