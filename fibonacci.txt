


"""Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.
The desired output is like :
fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]"""
a, b = 1, 1
list_fib = []
while a <= 55:
    list_fib.append(a)
    a, b = b, a + b
print(list_fib)

Or


startNumber = int(raw_input("Enter the start number here "))
endNumber = int(raw_input("Enter the end number here "))

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print map(fib, range(startNumber, endNumber))