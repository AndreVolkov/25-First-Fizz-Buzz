# 25 first "Fizz Buzz"

def FizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print('Fizz Buzz', end='=')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
    return FizzBuzz

i = 1
k = 0
while k != 25:
    if i % 3 == 0 and i % 5 == 0:
        k = k + 1
        print(k, end='. ')
        FizzBuzz(i)
        print(i)
    i = i + 1

