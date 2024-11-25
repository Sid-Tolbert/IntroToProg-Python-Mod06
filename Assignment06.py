# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Sid Tolbert,11.24.2024,Created Script
#   <Sid Tolbert>,<11.24.2024>,<Functions>
# ------------------------------------------------------------------------------------------ #

#__________________________________Import_Libraries____________________________________________________________________#
# Import required libraries
import json

#__________________________________Constants_and_Variables_____________________________________________________________#
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str = ''  # Hold the choice made by the user.
students: list = []  # a table of student data

#__________________________________Processing__________________________________________________________________________#
class FileProcessor:
    """
    A class of functions to process data input and output from files.

    ChangeLog: (Who, When, What)
    Sid Tolbert, 11.24.2024, FileProcessor class created

    """

    # When the program starts, read the file data into table
    # Extract the data from the file
    # Read from the Json file

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        A function that reads the content of a JSON file into a list.
        There is error handling in case there isn't a JSON file in the working directory.

        ChangeLog: (Who, When, What)
        Sid Tolbert, 11.24.2024, read_data_from_file function created

        :parameter file_name: str = This string is the name of the file to be read from
        :parameter student_data: list = list that file will be read into
        :return: student_data
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("File not found!", e)
        except Exception as e:
            IO.output_error_messages("An error occurred!", e)
        except Exception as e:
            print("Error: There was a problem with reading the file.")
            print("Please check that the file exists and that it is in a json format.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """

        :param file_name: str = This string is the name of the file to be written to
        :param student_data: list = list that will be written into the file
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

#__________________________________Presentation________________________________________________________________________#
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Sid Tolbert,11.24.2024,Created Class
    Sid Tolbert,11.24.2024,Added menu output and input functions
    Sid Tolbert,11.24.2024,Added a function to display the data
    Sid Tolbert,11.24.2024,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

            ChangeLog: (Who, When, What)
            Sid Tolbert,11.24.2024,Created function

            :return: None
            """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')
    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu of choices to the user

        ChangeLog: (Who, When, What)
        Sid Tolbert,11.24.2024,Created function

        :return: None
        """
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Sid Tolbert,11.24.2024,Created function

        :return: string with the users choice
        """

        try:
            menu_choice = input("What would you like to do: ")
            print()
            if menu_choice not in ("1","2","3","4"):
                raise Exception("Please only choose one of the menu choice numbers presented.")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return menu_choice

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function takes student data from the user and prints which student has been registered for which class

        ChangeLog: (Who, When, What)
        Sid Tolbert,11.24.2024,Created function

        :param student_data: list = This list contains the dictionaries of student data
        :return: student_data = returns the list of dictionaries
        """

        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("What course will the student be registered for? ")

            student = {"FirstName": student_first_name,
                   "LastName": student_last_name,
                   "CourseName": course_name}
            student_data.append(student)

            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function prints the student data that has been collected or pulled from the JSON file.

        ChangeLog: (Who, When, What)
        Sid Tolbert,11.24.2024,Created function

        :param student_data: list = list of student data with names and registered course
        :return: None
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
            f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

#_______________End_of_Function_Definitions____________________________________________________________________________#



#_______________________Script_________________________________________________________________________________________#

# Reads the current JSON file data into the student_data list
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the following tasks
while True:

    # Prints the block of menu choice text
    IO.output_menu(menu=MENU)

    # Collects the user input menu choice
    menu_choice = IO.input_menu_choice()

    # Menu choice 1 action
    if menu_choice == "1":

        # Collects the user input registration data and continues loop
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Outputs the current registration data and continues loop
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":

        # Writes the current registration data to the JSON file and continues loop
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue
    elif menu_choice == "4":

        # Stops and exits the loop
        break

print("Program Ended")
