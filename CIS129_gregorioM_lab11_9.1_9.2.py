# Gregorio Mangaoang
# 2 April 2025
# This program allows the user to enter as many grades as they want and when they choose to end it it will display the number of grades, average score, and the sum of all


MAX = 100
MIN = 0
DECI_LENGTH = 2
SENTINAL = -1

prompt = 'Enter a student grade: (-1 to END)'

def main():

    #Getting the student grade and storing to file / Can also run multiple times until the user chooses to end the program
    with open('grades.txt', mode='w+') as student_grade:
    
        while True:
            grade = get_valid_grade(prompt, SENTINAL, MAX, DECI_LENGTH)
            if grade == -1:
                break
            student_grade.write(f'{grade}\n')

    #This displaus the student grades at the end with the format of amount of grades entered, average of all the grades, and the sum of all grades
    with open('grades.txt', mode='r') as student_grade:
        count = 0
        sum = 0
        average = 0
        for lines in student_grade:
            lines = lines[:-1]
            print(lines)
            
            count +=1
            sum += float((lines))
            
        average = sum / count
            
        print(f'Number of grades: {count}')
        print(f'Average: {average:.2f}')
        print(f'Sum: {sum:.2f}')
    
#Input Validation functions

#First call to get the value from user
def get_valid_grade(message,low,high, decimal_length):
    new_value = get_float(message)
    
    while is_invalid(message,new_value,low,high,decimal_length):
        print(f'ERRROR: Must be between {MIN} and {MAX}')
        new_value = get_float(message)

    return new_value
    
#Making sure that the grade entered is a possinle grade
def is_invalid(msg,new_value,l,h,deci_length):
    if new_value >h:
        return True
    if new_value < l:
        return True
    if len(str(new_value).split('.')[1])> deci_length:
        return True

    return False

#To catch any inputs that is not an interger
def get_float(grade):
    while True:
        try:
            grade = float(input(prompt))
            return grade
        except ValueError:
            print('NOT Readable : Must be 0-100')
    
        
main()