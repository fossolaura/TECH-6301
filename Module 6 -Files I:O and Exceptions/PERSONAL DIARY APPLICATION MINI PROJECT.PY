# Requirements

# Create a simple personal diary application where users can write and 
# save their daily thoughts or experiences to a text file. The program 
# should allow users to view their previous entries and handle exceptions 
# in a controlled manner (e.g., file not found errors and permission issues).


import os
from datetime import datetime

DIARY_FILE_PATH = 'diary_entries.txt'

def add_diary_entry():
    entry_content = input("Write your diary entry:\n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} - {entry_content}\n\n"
    try:
        with open(DIARY_FILE_PATH, 'a') as file:
            file.write(entry)
        print("Diary entry added successfully.")
    except PermissionError:
        print("Permission denied: Unable to write to the diary file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_diary_entries():
    try:
        with open(DIARY_FILE_PATH, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("No diary entries found. Start by writing your first entry.")
    except PermissionError:
        print("Permission denied: Unable to read the diary file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\nPersonal Diary Application")
        print("1. Write new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_diary_entry()
        elif choice == '2':
            view_diary_entries()
        elif choice == '3':
            print("Exiting the diary application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
