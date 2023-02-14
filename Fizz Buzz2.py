# 25 first "Fizz Buzz"

def FizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        s = 'Fizz Buzz'
        
    elif n % 3 == 0:
        s = 'Fizz'
    elif n % 5 == 0:
        s = 'Buzz'
    else:
        s = n
    return s


i = 1
k = 0
while k != 25:
    s = FizzBuzz(i)
    if s == 'Fizz Buzz':
        k = k + 1
        print(k, s,'=', i)
        
    i = i + 1
