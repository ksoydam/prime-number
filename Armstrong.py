
number = input("Please enter an integer number: ")

power = len(number)

Output = 0

if number.startswith("-") or "." in number or "," in number or (not number.isdigit()):

    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

else:

    for i in number:

        Output += int(i) ** power

    if int(number) == Output:

        print(number + " is an Armstrong number")

    else:

        print(number + " is not an Armstrong number")
