def devide_num(a, b):
    if b == 0:
         raise ZeroDivisionError("Pay attention. You're trying devide by zero! Exchange second argument and try again")
    return a / b



while True:
    f_n = int(input("Enter num one: "))
    s_n = int(input("Enter num one: "))
    try:
        print(devide_num(f_n, s_n))
        message = input("Do you want to continue? ")
        if message == "yes":
            continue
        else:
            break
    except ZeroDivisionError as e:
        print(e)




    
