#Gregorio Mangaoang
#2 May 2025
#This program allows yous to store a students first name and last name with 3 of their exam grades

import csv
MIN = 0
MAX = 100  
decimal_length = 2

prompt = 'Enter Exam grade: '
RERUN = 'Would you like to put another Student grade (y/n): '

def main():
    with open('grades.csv' ,mode= 'w') as student_grade:
        grade_writer = csv.writer(student_grade, delimiter=',')
        
        SENTINAL = 'y'
        last_name = ''
        first_name = ''
        g1 = 0
        g2 = 0
        g3 = 0
        
        #sentinel while loop
        while SENTINAL != 'n':
            last_name = input('Enter last name: ')
            first_name = input('Enter First name: ')
            

            g1= get_valid_grade(prompt, MIN, MAX, decimal_length )
            g2= get_valid_grade(prompt,MIN, MAX, decimal_length )
            g3= get_valid_grade(prompt,MIN, MAX, decimal_length )
            
            grade_writer.writerow([last_name] + [first_name] + [g1] + [g2] + [g3])
            
            
            SENTINAL = getRerun(RERUN)

        #get values of variables from user
        
        #end while loop
        
# Input Validation for the sentinal (making sure that the user enters y/n to stop the program or enter another students info) <<<<<
def getRerun(message):
    new_value = check(message)
    
    while isnotyn(new_value):
        print('must be y/n')
        new_value = check(message)
        
    return new_value

# Checking if its the right string value
def isnotyn(message):
    if message == 'y' or message == 'n':
        return False

    return True

# Catching it if it's not a string value
def check(message):
    while True:
        try:
            grade = input(RERUN)
            grade = grade.lower()
            return grade
        except ValueError:
            print('NOT Readable : Must be y/n')
            
#>>>>>

#Input Validation for grade entered <<<<<
def get_valid_grade(message,low,high, decimal_length):
    new_value = get_float(message)
    
    while is_invalid(message,new_value,low,high,decimal_length):
        print(f'ERRROR: Must be between {MIN} and {MAX}')
        new_value = get_float(message)

    return new_value
    
# Catching grades that's not in the gradebook system 0-100
def is_invalid(msg,new_value,l,h,deci_length):
    if new_value >h:
        return True
    if new_value < l:
        return True
    if len(str(new_value).split('.')[1])> deci_length:
        return True

    return False

# Checking to see if the value entered was a interger
def get_float(grade):
    while True:
        try:
            grade = float(input(prompt))
            return grade
        except ValueError:
            print('NOT Readable : Must be 0-100')
    

#>>>>>
    
main()