# Module 4 Lab-4
# Gregorio Mangaoang
# 25 Febuary 2025
# It calculates the bonus for the employee and store according to sales increase

storeAmount = 0
empAmount = 0

keepGoing = 'y'
monthlySales = 0
storeBonus = 0
employeeBonus = 0
salesIncrease = 0
promt = "How much was the company's monthly sales? "

while keepGoing == 'y':
    monthlySales = float(input(promt))

    if monthlySales >= 110000: 
        storeBonus = 6000
    elif monthlySales >= 100000: 
        storeBonus = 5000
    elif monthlySales >= 90000: 
        storeBonus = 4000
    elif monthlySales >= 80000: 
        storeBonus = 3000
    else: 
        storeBonus = 0
        
    salesIncrease = float(input('Sales increase?'))
    salesIncrease = salesIncrease / 100

    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else: 
        empAmount = 0
        
    print("The store bonus amount is $", storeBonus)
    print("The employee bonus amount is $", empAmount)
    if (storeBonus == 6000) and (empAmount == 75):
        print('Congrats! You have reached the highest bonus amounts possible! ')
        
    keepGoing = input('Do you want to run the program again? (Enter y or n)')
    