# ------------------------------------------------------------------------------------------ #
# Title: Assignment02
# Desc: This assignment demonstrates using constants, variables,
#         operators, formatting, and files
# and calculations
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
COURSE_NAME: str = "Python 100"
COURSE_PRICE: float = 999.98  # Don't use a string for this data for you will get a format() error
STATE_TAX:float = .09
TOTAL_PRICE:float = COURSE_PRICE + (COURSE_PRICE * STATE_TAX)
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
csv_data: str = ''  # Holds combined string data separated by a comma.
file_obj = None  # Holds a reference to an opened file.

# Get data from the user
student_first_name = input("Enter the student's first name: ")
student_last_name = input("Enter the student's last name: ")

# Present the data to the user
csv_data += f"{student_first_name},{student_last_name}," \
            f"{COURSE_NAME},{COURSE_PRICE:.2f}," \
            f"{TOTAL_PRICE:.2f}\n"
print(csv_data)

# Process the data to a file
file_obj = open(FILE_NAME, "w")
file_obj.write(csv_data)
file_obj.close()

