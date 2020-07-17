#Exercise 1.11 correction for overpayment

principal = 500000.0
rate = 0.05
payment = 2684.11
last_payment = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0
num_payments = 0

while principal > 0:
    while num_payments < extra_payment_start_month:
        principal= principal * (1+rate/12) - payment
        num_payments = num_payments + 1
        total_paid = total_paid + payment
        print(num_payments, total_paid, principal)
    while (extra_payment_start_month - 1) > num_payments or num_payments < (extra_payment_end_month + 1):
        principal = principal * (1+rate/12) - payment - extra_payment
        num_payments = num_payments + 1
        total_paid = total_paid + payment + extra_payment
        print(num_payments, total_paid, principal)
    while principal > payment:
        principal = principal * (1+rate/12) - payment
        num_payments = num_payments + 1
        total_paid = total_paid + payment
        print(num_payments, total_paid, principal)
    last_payment = principal * (1+rate/12)
    principal =  principal * (1+rate/12) - last_payment
    num_payments = num_payments + 1
    total_paid = total_paid + last_payment
    print(num_payments, total_paid, principal)

print('Total paid', total_paid)
print('Months', num_payments)

