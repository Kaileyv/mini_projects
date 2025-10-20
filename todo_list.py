
todo_list = [] # Initialize an empty to-do list

while True:
    # Display menu options
    print("------------------------------------------")
    print("To-Do List Menu:")
    print("A - Add a Task")
    print("V - View To-Do list")
    print("D - Delete a Task")
    print("Q - Quit To-Do list Program")

    # Get user input
    user_option = input("Select an option (A, V, D, or Q): ").upper()

    # Process user input - A, V, D, Q
    if user_option == "A":                                            # Add a Task
        task = input("Enter a task to add: ")                         # Get task name from user to add
        todo_list.append(task)                                        # Add task to the to-do list
        print(f'Task "{task}" added to the list.')                   
    elif user_option == "V":                                          # View To-Do list  
        if not todo_list:                                             # Check if the to-do list is empty
            print("To-Do list is empty.")
        else:
            print("[: ~ TO-DO LIST ~ :]")                             
            c = 1
            for i in todo_list:
                print(f"{c}. {i}")                                    # Display the to-do list in numbered format
                c+=1
    elif user_option == "D":                                          # Delete a Task  
        delete = int(input("Enter the task number to delete: "))      # Get task number from user to delete
        if 0 < delete <= len(todo_list):                              # Check if the task number is valid
            del todo_list[delete - 1]                                 # Delete the task from the to-do list based on index
            print(f"Task number {delete} is deleted from the list.")
        else:
            print("Invalid task number.")
    elif user_option == "Q":                                          # Quit To-Do list Program  
        print("Quitting To-Do list program! Toodles!")
        break
    else:
        print("Invalid option. Please choose A, V, or D.")            # Handle invalid user input