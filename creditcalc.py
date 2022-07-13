import math
import argparse
import sys
import numpy as np

args = sys.argv

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["diff", "annuity"], required=True, help="type")
parser.add_argument("-pay", "--payment", type=int)
parser.add_argument("-pri", "--principal", type=int)
parser.add_argument("-per", "--periods", type=int)
parser.add_argument("-i", "--interest", type=float)

#body of the function
##checking for minimum 4 arguments
if len(args) < 5:
    print("Incorrect parameters.")
else:
    args = parser.parse_args()
    if args.interest is None:
        print('Incorrect parameters')
    elif args.type == "annuity":
        i = args.interest / (12 * 100)
        if args.payment is None:
            payments_1 = (args.principal * ((i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1)))
            print(payments_1)
        elif args.principal is None:
            loan_principal = args.payment / ((i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1))
            print(loan_principal)
        else:
            base = 1 + i
            number_of_month = math.ceil(math.log(args.payment / (args.payment - i * args.principal), base))
            years = number_of_month // 12
            month = number_of_month % 12
            overpay = (args.payment * number_of_month) - args.principal
            print(f'It will take {years} years to repay this loan\nOverpayment = {overpay}')
    elif args.type == "diff":
        o = []
        i = args.interest / (12 * 100)
        def calc(a):
            months = range(1, args.periods + 1)
            c = []
            for m in months:
                result = m
                res = math.ceil(args.principal / args.periods + i * (args.principal -
                                                                     (args.principal * (m - 1) / args.periods)))
                c.append(res)
                print(f'Month {result}: payment is {res}')
            return c
        length = np.sum(calc(o))
        overpay = length - args.principal
        print(f'Overpayment = {overpay}')
    else:
        print("Incorrect parameters")
