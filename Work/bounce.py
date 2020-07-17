# bounce.py
#
# Exercise 1.5
ini_height = 100
fin_height = 0
num_bounce = 0
while num_bounce < 10:
    
    num_bounce = num_bounce + 1
    fin_height = (3/5)* ini_height
    print(num_bounce, fin_height)
    ini_height = fin_height
