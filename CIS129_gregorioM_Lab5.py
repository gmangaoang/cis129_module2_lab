totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'

while keepGoing == 'y':
    totalBottles = 0
    todayBottles = 0
    counter = 1

    nbr_of_days = 7
    
    while nbr_of_days >= counter:
        print("Enter number of bottles for day:", counter)
        todayBottles = int(input())
        totalBottles = totalBottles + todayBottles
        counter+=1
        
        totalPayout = totalBottles * .10
        
        
    print("The total numbers of bottles:", totalBottles)
    print("The total payout is:",f'{totalPayout:>.2f}',)
    
        
    keepGoing = input('Would you like to run the program again? (Enter y or n)')    
    