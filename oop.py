entered_number = int(input("Enter a number please: "))

num = 2

while num <= entered_number:
    i = 2
    is_aval = True

    while i < num:
        if num % i == 0:
            is_aval = False
            break
        i += 1

    if is_aval:
        print(num)

    num += 1