'''Fibonacci series using dp'''


def fib(a):
    n=[0,1]
    for i in range(2,a+1):
        n.append(n[i-1]+n[i-2])

    return n[a]


print(fib(10))
'''
def fib(n):
    arr=[0]*n
    a,b=0,1
    if arr
    for i in range(n):
        arr[i]=a
        a,b=b,a+b
    print(arr)
    return a


print(fib(4))'''
