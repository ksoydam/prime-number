



"""Task : Print the prime numbers which are between 1 to entered limit number (n).
You can use a nested for loop.
Collect all these numbers into a list
The desired output for n=100 :
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
61, 67, 71, 73, 79, 83, 89, 97]"""


def main(n):
    list_prime = []
    for i in range(2, n+1):
        divider = 0
        for x in range(2, i):
            if not i % x:
                divider += 1
                break
        if not divider:
            list_prime.append(i)
    print(list_prime)


n = int(input("Enter an end number : "))
main(n)