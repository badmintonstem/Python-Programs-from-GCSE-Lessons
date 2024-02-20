def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

while True:
    valid = False
    while valid == False:
        valid = True
        num = input("Enter a number: ")
        if not num.isnumeric():
            print("Invalid data entry.")
            valid = False
    print(num+"! = ",factorial(int(num)))
