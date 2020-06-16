from math import ceil, log, floor
import argparse


def calc_months():
    monthly_payments = int(input("Enter monthly payment:"))
    repay = ceil(get_principal() / monthly_payments)
    print(f"It takes 7 months to {repay} the credit")


def get_payment(months):
    return get_principal() / months


def calc_lastpayment(months, payment):
    return get_principal() - (months - 1) * payment


def get_nominal_interest(credit_interest):
    return (credit_interest / 100) / (12 * (100 / 100))


# def calc_mpayments():
#     months = int(input("Enter count of months:"))
#     payment = get_payment(months)
#     if isinstance(payment, float):
#         print(f"Your monthly payment = {ceil(payment)} with last month "
#               f"payment = {ceil(calc_lastpayment(months, ceil(payment)))}.")
#     else:
#         print(f"Your monthly payment = {ceil(payment)}")
#
#
def get_principal(payment, periods, interest):
    i = get_nominal_interest(interest)
    principal_dem = (i * (pow((1 + i), periods))) / (pow((1 + i), periods) - 1)
    get_princi = payment / principal_dem

    print(f"Your credit principal = {floor(get_princi)}!")
    print(f"Overpayment = {(payment * periods) - floor(get_princi)}")


def get_months(principal, payment, interest):
    nominal_interest = get_nominal_interest(interest)
    num = payment / (payment - (nominal_interest * principal))
    num_months = log(num, (1 + nominal_interest))
    years = ceil(num_months) // 12
    months = ceil(num_months) % 12
    if months == 0:
        print(f"You need {years} years to repay this credit!")
    elif months > 0:
        print(f"You need {years} years and {months} months to repay this credit!")
    print(f"Overpayment = {((years * 12 + months) * payment) - principal}")


def get_annuity(principal, periods, interest):
    interest = get_nominal_interest(interest)
    annuity = principal * ((interest * pow(1 + interest, periods) /
                            (pow(1 + interest, periods) - 1)))

    print(f"Your annuity payment is {ceil(annuity)}!")
    print(f"Overpayment = {round((ceil(annuity) * periods) - principal)}")


def get_diff(principal, periods, interest):
    nominal_i = get_nominal_interest(interest)
    sum_paid = 0
    for i in range(1, periods + 1):
        paid = ((principal / periods) + nominal_i * (principal - ((principal * (i - 1)) / periods)))
        sum_paid = sum_paid + ceil(paid)
        print(f"Month {i}: paid out {ceil(paid)}")
    print()
    print(f"Overpayment = {ceil(sum_paid - principal)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=["annuity", "diff"])
    parser.add_argument("--principal", type=int)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--payment", type=float)
    args = parser.parse_args()
    if args.type == "annuity":
        if args.interest is None or (len(vars(args)) < 4):
            print("Incorrect parameters")
        elif args.payment is not None and args.interest is not None and args.periods is not None:
            get_principal(args.payment, args.periods, args.interest)
        elif args.principal is not None and args.periods is None:
            get_months(args.principal, args.payment, args.interest)
        else:
            get_annuity(args.principal, args.periods, args.interest)
    elif args.type == "diff":
        if len(vars(args)) < 4 or args.payment is not None or args.interest is None:
            print("Incorrect parameters")
        else:
            get_diff(args.principal, args.periods, args.interest)


main()
