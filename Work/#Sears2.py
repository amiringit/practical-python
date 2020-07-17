#Sears2.py
bill_thickness = .11 * .001     #Meters
num_bills = 0
day = 0
sears_height = 421  #Meters

while num_bills * bill_thickness < sears_height:
    num_bills = num_bills * 2
    day = day + 1
    
print('Number of days', day)
print('Number of bills', num_bills)
print('Height reached', bill_thickness * num_bills)