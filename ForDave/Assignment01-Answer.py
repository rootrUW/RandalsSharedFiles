# ------------------------------------------------------------------------------------------ #
# Title: Assignment01
# Desc: This assignment demonstrates using constants, variables, and print()
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
COURSE_NAME: str = "Python 100"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.

# Get data from the user
student_first_name = input("Enter the student's first name: ")
student_last_name = input("Enter the student's last name: ")

# Present the data to the user

#print(student_first_name, student_last_name, 'is registered for')

#print(student_first_name, student_last_name + ' ' + 'is registered for' + ' ' + COURSE_NAME)

print(student_first_name + ' ' + student_last_name + ' ' + 'is registered for' + ' ' + COURSE_NAME)


