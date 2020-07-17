#Exercise 1.7 Mortgage

principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Totalpaid', total_paid)
