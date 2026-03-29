n = int(input("Enter the number: "))

if n < 1:
    print("Not a prime number")
else:
    for i in range(2,n):
        if n % 2 == 0:
            print("Not a prime number")
            break
        else:
            print("Prime number")