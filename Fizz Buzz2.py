# 25 first "Fizz Buzz"

def FizzBuzz(n):
    i = 1
    k = 0
    while k != n:
        if i % 3 == 0 and i % 5 == 0:
            k = k + 1
            print(k,'Fizz Buzz -',i)
        i = i + 1
FizzBuzz(25)

