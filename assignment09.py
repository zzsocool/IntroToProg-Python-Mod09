# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# <Your Name>,<Today's Date>,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules

if __name__ == '__main__':

    import ProcessingClasses as PC
    import IOClasses as IOC
else:
    raise Exception("Modules not found")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program
strFileName = 'EmployeeData.txt'
lstOfProductObjects =[]
obj=[]
obj2=[]
try:
    lstOfProductObjects = PC.FileProcessor.read_data_from_file(strFileName)

    while True:
        IOC.EmployeeIO.print_menu_items()
        strChoice = IOC.EmployeeIO.input_menu_options()
        if strChoice.strip()=='1':
            IOC.EmployeeIO.print_current_list_items(lstOfProductObjects)
            continue
        elif strChoice.strip()=='2':
            lstOfProductObjects.append(IOC.EmployeeIO.input_employee_data())

            continue
        elif strChoice.strip()=='3':
            PC.FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
            continue
        elif strChoice.strip()=='4':
            break
except Exception as e:
    print('There was error! Check file permissions.')
    print(e,e.__doc__,type(e),sep='\n')

# Main Body of Script  ---------------------------------------------------- #
