def pass_check(password):
    # password=input("Enter the password :")
    upper_count, lower_count, digit_count, special_count, flag = 0, 0, 0, 0, 0
    while True:
        if (len(password) < 6 or len(password) > 12):
            print("Please enter a passoword in between 6-12 char long!")
        else:
            for ch in password:
                if (ch.isupper()):
                    upper_count += 1
                if (ch.islower()):
                    lower_count += 1
                if (ch.isdigit()):
                    digit_count += 1
                if (ch in ('$', '#', '@')):
                    special_count += 1
        if (upper_count >= 1 and lower_count >= 1 and digit_count >= 1 and special_count >= 1):
            print("Password is valid")
            flag = 1
            break
        else:
            print("Password is invalid")
            password = input("Renter the password :")
            flag = 0
    if flag == 1:
        return 1
    else:
        return 0
#print(pass_check('Python@123'))