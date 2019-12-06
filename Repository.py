
import csv
import os
import sys
import time



#Name: Monika Pusz
#Date: 5/07/2018
#Course: Comupter Science


def displayIntro():
    time.sleep(1)
    print("Research publications repository\n ")

########################
# Clear Console/Window #
########################
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():

    # Display the header
    print("PLEASE UPLOAD FILE WITH REPOSITORY  \n")

    # Create object to access class
    repository = Repository()
    # Let user load csv repository file
    repository.get_user_files()


    while True:
        # Ask user to input value
        userInput = input("\nResearch publications repository\n\nPlease enter: \n\n1. Add a new publication \n2. Delete publication from the system \n3. Display list \n4. Close Program\n\n  ")
        # Return option to add new publication
        if userInput == "1":
            # Clear the screen
            clear_console()
            # Call function to add new publication
            repository.add_publication()

        elif userInput == "2":
            # Clear the window
            clear_console()
            # Call function to delete publication
            repository.delete_publication()

        elif userInput == "3":
            # Clear the window
            clear_console()
            # Call function to display csv file
            repository.display_list()

        elif userInput == "4":
            # Close the program
            sys.exit()

        else:
            print("\nError! Please enter correct number again!\n")




class Repository:

    # Access root directory and remove irrelevant files
    global repository
    repository = os.listdir()
    if '.idea' in repository:
        repository.remove('.idea')
    if 'main.py' in repository:
        repository.remove('main.py')
    if '.git' in repository:
        repository.remove('.git')


    def get_user_files(self):

        while True:
            # Display files in root directory
            for list_position, file_name in enumerate(repository):
                print(list_position, "-", file_name)
            # User selection from the list
            userInput = input("\n\n ")
            # Check if user input is valid
            if (int(userInput) < 0) or (int(userInput) > len(repository)):
                print("Invalid Input. Try again. \n")
            else:
                # Display message to user if successful
                print("\nLoading successful!")
                time.sleep(1)
                break
        # Create global variable
        global repository_file

        # Store repository file loaded by user (globally)
        repository_file = repository[int(userInput)]
        # Remove file from the root directory list
        repository.remove(repository_file)


        # Check if csv file contains any publication older than 5 years
        # Open file for reading
        with open(repository_file, 'r') as in_file:
            csv_in = list(csv.reader(in_file))
            # Create list for new csv list to add only valid values
            filtered_list = []
            # Append header in new csv list
            filtered_list.append(csv_in[0])
            # Read each line in csv file (starting from row[1] - skipping headers)
            for row in csv_in[1:]:
                # Check rows with publications that have been published in the last 5 years
                if int(row[2]) >= 2013:
                    # Save each row into list
                    filtered_list.append(row)

            # Open file for writing
            with open(repository_file, 'w', newline='') as out_file:
                writer = csv.writer(out_file)
                # Write list elements into csv file
                writer.writerows(filtered_list)

        clear_console()

    def display_list(self):

        # Display header
        print("LIST OF PUBLICATIONS: \n")

        # Open file for reading
        with open(repository_file, 'r') as csvDataFile:
            repository_reader = list(csv.reader(csvDataFile))
            # Create list to store headers
            header= []
            # Add headers to the list
            header.append(repository_reader[0])
            # Remove '[]' from the headers
            print(str(header).strip('[]'))

            # Read each line, skipping headers
            for row in repository_reader[1:]:
                # Sort the list in alphabet order
                sort = sorted(repository_reader[1:])
                # Read each line, display sorted list
                for c, value in enumerate(sort, 1): #Display list from position 1
                    print(c, "-", str(value).strip('[]'))
                break
            print("\n")



    def add_publication(self):

        # Open csv file for writing, 'a' - append
        with open(repository_file, 'a', newline='') as new_file:  #
            csv_writer = csv.writer(new_file, quoting=csv.QUOTE_ALL)
            while (1):
                # Ask user to enter new book details
                print("Please enter details of new publication:\n ")
                surname = input("Author Surname: ")
                name = input("First Name: ")
                # Raise an Exception if input is not an integer
                try:
                    year = int(input("Year of Publication: "))
                except ValueError:
                    print("\nError! The Year of Publication must be an integer value. \n")
                    time.sleep(1)
                    clear_console()
                    continue
                # Check if the book entered is less than 5 years old
                if int(year) <= 2013:
                    print("\nError! No book older than 5 years is allowed in the system")
                    print("Please try again\n")
                    time.sleep(1)
                    clear_console()
                    continue
                elif int(year) > 2018:
                    print("Invalid input! Please enter valid year of publication. ")
                    time.sleep(1)
                    clear_console()
                    continue
                title = input("Title: ")
                publisher = input("Publisher: ")

                # Write new line publication into csv file
                csv_writer.writerow([surname.upper(), name.upper(), year, title.upper(), publisher.upper()])
                print("\nNew book has been added to the system! \n")
                time.sleep(1)
                break
            clear_console()


    def delete_publication(self):

        # Display header
        print("LIST OF PUBLICATIONS: \n")

        # Open csv file for reading
        with open(repository_file, 'r') as csvDataFile:
            repository_reader = list(csv.reader(csvDataFile))
            # Create list to store header
            header = []
            # Save header into the list
            header.append(repository_reader[0])
            # Remove '[]' from the headers (so output looks nicer)
            print(str(header).strip('[]'))

            # Read each line , skip header
            for row in repository_reader:
                # Sort the list in alphabetical order
                sort = sorted(repository_reader[1:])
                # Display sorted list from position 1, remove '[]' from each line
                for list_position, publication in enumerate(sort, 1): #Display list from position 1
                    print(list_position, "-",  str(publication).strip('[]'))
                while True:
                    userInput = input("\nPlease enter the position of the publication to be removed from the system:\n\n")
                    # Check if user input is valid integer
                    if int(userInput) < 1 or int(userInput) > len(sort):
                        print("Invalid input! Try again \n")

                    else:
                        break

                # Create a list
                in_file = []
                # Save row chosen by user
                in_file.append(sort[int(userInput) - 1])
                # Remove the line from the file
                sort.remove(sort[int(userInput) - 1 ])

                # Open file for writing
                with open(repository_file, 'w', newline='') as out_file:
                    writer = csv.writer(out_file)
                    #Write header into file
                    writer.writerow(repository_reader[0])
                    # Write new data into file
                    writer.writerows(sort)
                print("\nBook has been removed from the system. ")
                time.sleep(1)
                break
            clear_console()




displayIntro()

if __name__ == "__main__": main()
