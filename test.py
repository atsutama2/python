import sys

print("hello world", end="")
sys.stdout.write("hello world\n")

# 各種演算
print('2+1 =', 2+1)
print('10-3 =', 10-3)
print('7*4 =', 7*4)
print('5/2 =', 5/2)
print('5//2 =', 5//2)
print('10%3 =', 10%3)
print('2**10 =', 2**10)

# 九九表
for x in range(0,9):
    for y in range(0,9):
        print('{0}'.format('%2d ' % ((x+1) * (y+1))), end="")
        print('')