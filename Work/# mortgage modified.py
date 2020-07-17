# mortgage modified

principal = 500000.0
rate = 0.05
payment = 2684.11
payment_l = 3684.11
total_paid = 0.0
num_payments = 0

while principal > 0:
    while num_payments < 12:
        principal = principal * (1+rate/12) - payment_l
        total_paid = total_paid + payment_l
        num_payments = num_payments + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    num_payments = num_payments + 1

print('Total paid:', total_paid, 'Number of payments:', num_payments)
