# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# HJong, 5/13/2021, Started script
# HJong, 5/13/2021, Created functions in Processor class
# HJong, 5/14/2021, Modified if statements in options 1 - 4 in the main program
# HJong, 5/14/2021, Added DocString within the functions in Processor class
# HJong, 5/14/2021, Added if statement in remove_data_from_list function to control task input
# HJong, 5/15/2021, Added if statement in add_data_to_list function to control task input
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = 'ToDoList.txt'  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ''  # Captures the user option selection
strTask = ''  # Captures the user task data
strPriority = ''  # Captures the user priority data
strStatus = ''  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, 'r')
        for line in file:
            task, priority = line.split(',')
            row = {'Task': task.strip(), 'Priority': priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'successful'

    @staticmethod
    def add_data_to_list(task_input, priority_input, list_of_rows):
        """ Add data into existing list of dictionary

        :param task_input: (string) of new task name
        :param priority_input: (string) of new task priority
        :param list_of_rows: (list) of dictionary rows to add new data to
        :return: (list) of dictionary rows
        """
        found = False
        cnt = 0
        return_status = 'successful'
        for row in list_of_rows:
            task_in_row, priority_in_row = row.values()
            if task_input == task_in_row:   # Check for new task against existing task
                found = True
                answer = IO.input_yes_no_choice('Oops, task exists! Do you want to replace the task? [Y/N]: ')
                if answer == 'y':
                    list_of_rows[cnt]['Priority'] = priority_input
                else:
                    return_status = 'cancelled'
                break
            cnt += 1
        if not found:
            dic_new_row = {'Task': task_input, 'Priority': priority_input}
            list_of_rows.append(dic_new_row)
        return list_of_rows, return_status

    @staticmethod
    def remove_data_from_list(task_update, list_of_rows):
        """ Remove data from existing list of dictionary

        :param task_update: (string) of task name to remove
        :param list_of_rows: (list) of rows of dictionary to remove data from
        :return: (string) of updated task name
        :return: (list) of dictionary rows
        """
        found = False
        return_status = 'successful'
        while not found:
            for row in list_of_rows:
                task_list, priority_list = row.values()
                if task_list == task_update:
                    list_of_rows.remove(row)
                    found = True
            if not found:
                answer = IO.input_yes_no_choice('Oops! Task does not exist. Do you want to re-enter [Y/N]: ')
                if answer == 'y':
                    task_update = IO.input_task_to_remove()
                    continue
                else:
                    return_status = 'cancelled'
                    break
        return task_update, list_of_rows, return_status

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Write data of existing list of dictionary to the file

        :param file_name: (string) name of the file to write data into
        :param list_of_rows: (list) you want to save into the file
        :return: (list) of dictionary rows
        """
        objFile = open(file_name, 'w')
        for row in list_of_rows:
            objFile.write(row['Task']+','+row['Priority']+'\n')
        return list_of_rows, 'successful'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionary rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print('******* The current Tasks ToDo are: *******')
        for row in list_of_rows:
            print(row['Task'] + ' (' + row['Priority'] + ')')
        print('*******************************************')
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :param message: (string) of message to user for entering '[Y/N]'
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Receive user input of task and priority to add

        :return: a tuple (task_choice, priority_choice)
        """
        task_choice = str(input('Enter the task name you want to add: ')).strip()
        priority_choice = str(input('Enter the priority of the task: ')).strip()
        return task_choice, priority_choice

    @staticmethod
    def input_task_to_remove():
        """ Receive user input of task to remove

        :return: string task_choice
        """
        task_choice = str(input('Enter the task name you want to remove: ')).strip()
        return task_choice

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()   # Receive task name and priority to add from user
        lstTable, status = Processor.add_data_to_list(task, priority, lstTable)     # Add data into the list table
        strStatus = 'Adding the task \''+task+'\' was '+status+'\n'
        IO.input_press_to_continue(strStatus)   # Display the status after the action
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()    # Receive task name to remove from user
        task, lstTable, status = Processor.remove_data_from_list(task, lstTable)    # Remove data from the list table
        strStatus = 'Removing the task \''+task+'\' was ' + status + '\n'
        IO.input_press_to_continue(strStatus)   # Display the status after the action
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")  # Ask the user for confirmation
        if strChoice.lower() == "y":    # If user confirm, save the file
            lstTable, status = Processor.write_data_to_file(strFileName, lstTable)
            strStatus = 'Saving data to file \''+strFileName+'\' was '+status+'\n'
            IO.input_press_to_continue(strStatus)
        else:   # If the user cancel, do not perform saving, and display the action is cancelled
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':    # If the user confirms, reload the file
            listTable, status = Processor.read_data_from_file(strFileName, lstTable)
            strStatus = 'Reloading the file '+strFileName+' was '+status+'\n'
            IO.input_press_to_continue(strStatus)
        else:   # If the user cancels, do not perform reloading, and display the action is cancelled
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break   # and Exit
