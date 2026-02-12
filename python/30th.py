num = int(input("Enter a number here: "))

if num <= 1:
    print("It is not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
