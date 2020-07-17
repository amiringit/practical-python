#Exercise 1.8 mortgage with extra payments

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 3684.11
num_payments = 0
total_paid = 0

while principal > 0:
    while num_payments < 12:
        principal = principal * (1+rate/12) - extra_payment
        num_payments = num_payments + 1
        total_paid = total_paid + extra_payment
    principal = principal * (1+rate/12) - payment
    num_payments = num_payments + 1
    total_paid = total_paid + payment

print('Total paid', total_paid,'Number of payments', num_payments)

