import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--principal", action="store", default=None, type=float,
                    help="Enter the loan principal")
parser.add_argument("--periods", action="store", default=None, type=float,
                    help="Enter the number of months needed to repay the loan. It's calculated based on "
                                                                  "the interest, annuity payment, and principal.")
parser.add_argument("--interest", action="store", default=None, type=float,
                    help="Enter the interest rate - is specified without a percent sign. Note that it can accept a "
                         "floating-point value. The loan calculator can't calculate the interest, "
                         "so it must always be provided.")
parser.add_argument("--payment", action="store", default=None, type=float,
                    help="Enter the payment amount. ")

args = parser.parse_args()

# Calculating the Number of Monthly Payments: --periods
# Example Parameters: --principal=1000000 --payment=15000 --interest=10
if args.periods == None and None not in (args.principal,args.interest,args.payment):
    i = args.interest/(12*100)
    n = math.ceil(math.log(args.payment/(args.payment-(i * args.principal)), 1+i))
    y = divmod(n, 12)
    print(f"It will take {int(y[0])} years and {math.ceil(y[1])} months to repay the loan!")

# Calculating the monthly payment (annuity)
# Example Parameters: --principal=1000000 --periods=60 --interest=10
if args.payment == None and None not in (args.principal, args.interest, args.periods):
    i = args.interest/(12*100)
    d = math.ceil((((1+i)**args.periods)*i*args.principal) / (((1+i)**args.periods)-1))
    print(f'Your monthly payment = {d}!')

# Calculating Loan Principal
# Example Parameters: --payment=8721.8 --periods=120 --interest=5.6
if args.principal == None and None not in (args.interest, args.payment, args.periods):
    i = args.interest/(12*100)
    p = round((args.payment*(((1+i)**args.periods)-1)) / (((1+i)**args.periods)*i))
    print(f'Your loan principal = {p}!')