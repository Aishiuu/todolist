# Importing the modules
import sqlite3
import datetime

# Creating the database connection
conn = sqlite3.connect("todo.db")
c = conn.cursor()

# Creating the table if it does not exist
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER PRIMARY KEY,
    task_name TEXT NOT NULL,
    created_on DATE NOT NULL,
    status TEXT NOT NULL
    )""")

# A function to create a new task
def create_task():
    # Asking the user for the task name
    task_name = input("Enter the task name: ")
    # Getting the current date
    created_on = datetime.date.today()
    # Setting the default status as pending
    status = "Pending"
    # Inserting the task into the table
    c.execute("INSERT INTO tasks (task_name, created_on, status) VALUES (?, ?, ?)", (task_name, created_on, status))
    # Committing the changes
    conn.commit()
    # Printing a confirmation message
    print("Task created successfully!")

# A function to delete a task
def delete_task():
    # Asking the user for the task id
    task_id = int(input("Enter the task id: "))
    # Deleting the task from the table
    c.execute("DELETE FROM tasks WHERE task_id = ?", (task_id,))
    # Committing the changes
    conn.commit()
    # Printing a confirmation message
    print("Task deleted successfully!")

# A function to show all the tasks
def show_tasks():
    # Querying the table for all the tasks
    c.execute("SELECT * FROM tasks")
    # Fetching the results
    tasks = c.fetchall()
    # Printing the tasks in a tabular format
    print("Task ID\tTask Name\tCreated On\tStatus")
    print("-" * 40)
    for task in tasks:
        print(f"{task[0]}\t{task[1]}\t{task[2]}\t{task[3]}")

# A function to mark a task as done
def mark_task():
    # Asking the user for the task id
    task_id = int(input("Enter the task id: "))
    # Updating the status of the task to done
    c.execute("UPDATE tasks SET status = 'Done' WHERE task_id = ?", (task_id,))
    # Committing the changes
    conn.commit()
    # Printing a confirmation message
    print("Task marked as done!")

# A function to display the menu
def display_menu():
    # Printing the menu options
    print("Welcome to the to-do list app!")
    print("Please choose an option:")
    print("1. Create a new task")
    print("2. Delete a task")
    print("3. Show all the tasks")
    print("4. Mark a task as done")
    print("5. Exit the app")

# A loop to run the app
while True:
    # Displaying the menu
    display_menu()
    # Asking the user for their choice
    choice = int(input("Enter your choice: "))
    # Executing the corresponding function
    if choice == 1:
        create_task()
    elif choice == 2:
        delete_task()
    elif choice == 3:
        show_tasks()
    elif choice == 4:
        mark_task()
    elif choice == 5:
        # Closing the database connection
        conn.close()
        # Breaking the loop
        break
    else:
        # Printing an error message
        print("Invalid choice. Please try again.")
