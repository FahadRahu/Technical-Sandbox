import math

print("Enter the loan principal:")
principal = int(input())
print("What do you want to calculate?")
print("type \"m\" for number of monthly payments,")
print("type \"p\" for the monthly payment:")

calc_type = input()
if calc_type == 'm':
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    months = math.ceil(principal / monthly_payment)
    print('')
    if months == 1:
        print(f"It will take 1 {months} month to repay the loan")
    else:
        print(f"It will take {months} months to repay the loan")
elif calc_type == 'p':
    print("Enter the number of months:")
    months = int(input())
    monthly_payment = math.ceil(principal / months)
    last_payment = principal - (months - 1) * monthly_payment
    if last_payment == monthly_payment:
        print(f"Your monthly payment = {monthly_payment}")
    elif last_payment < monthly_payment:
        print(f"Your monthly payment = {monthly_payment} and the last payment = {last_payment}")