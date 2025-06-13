#! python3
import sys
import json
from pathlib import Path


def instructions():
    print("To use this Personal To Do List please follow the instructions below:")
    print("Type 'Add [task]' to add a task to the list.")
    print("Type 'tasks' to see all your tasks in the list.")
    print("Type 'Mark [task-number]' to mark a task as done.")
    print("Type 'Remove [task-number]' to delete a task from the list.")
    print("To get the task number of a task type 'tasks' \n.")
    print("Type 'Save' to save your to-do-list\n")
    print("If you would like to run the application as a script or from windows dialog box just add the filename before any of the commands. Example:")
    print("'to_do_list.py Add Wash Car' or 'to_do_list.py Mark 2' or 'to_do_list.py tasks' or 'to_do_list.py Remove 5' \n")
    print("You may also specifically run a particular command  upon running the program. Example:")    
    print(f"'to_do_list.py Add Go to the Market' will add the task 'Go to the Market' to the to-do-list upon running the program.\n")
    print("Type 'instructions' to see full list of instructions\n")
    print("Type 'close' to end the program at any point.")

def readInput():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command.lower() == "tasks":
            return "tasks"
        elif command.lower() == "mark":
            if len(sys.argv) != 3:
                return "error"
            try:
                int(sys.argv[2])
            except(ValueError):
                return "error"
            if int(sys.argv[2]) > len(to_do_list):
                print("No task with number " + sys.argv[2])
                return "error"
            return ("mark", int(sys.argv[2]))
        elif command.lower() == "remove":
            if len(sys.argv) != 3:
                return "error"
            try:
                int(sys.argv[2])
            except(ValueError):
                return "error"
            if int(sys.argv[2]) > len(to_do_list):
                print("No task with number " + sys.argv[2])
                return "error"
            return ("remove", int(sys.argv[2]))
        elif command.lower() == "add":
            if len(sys.argv) < 3:
                return "error"
            task = " ".join(sys.argv[2:])
            return ("add", task)
        elif command.lower() == "instructions":
            return "instructions"
        else:
            return "error"
    else:
        print("Give a command to view, add, mark or remove one of your tasks")
        command = input("Your command?: ").lower()
        if command.lower() == "close":
            return "close"
        elif "add" in command:
            command_list = command.split(" ")
            if command_list[0].lower() != "add":
                return "error"
            for command in command_list:
                if command == " ":
                    command_list.remove(command)
            task = " ".join(command_list[1:])
            print(task)
            return("add", task)

        elif "mark" in command:
            command_list = command.split(" ")
            if command_list[0].lower() != "mark":
                return "error"
            for command in command_list:
                if command == "":
                    command_list.remove(command)
            if len(command_list) != 2:
                return "error"
            try:
                int(command_list[1])
            except(ValueError):
                return "error"
            if int(command_list[1]) > len(to_do_list):
                print("No such Task with number " + command_list[1] + " exists")
                return "error"
            return (command_list[0], int(command_list[1]))
        elif "remove" in command:
            command_list = command.split(" ")
            print(command_list)
            if command_list[0].lower() != "remove":
                return "error"
            new_command = []
            for command in command_list:
                if command == "":
                    command_list.remove(command)
                    
            if len(command_list) != 2:
                return "error"
            try:
                int(command_list[1])
            except(ValueError):
                return "error"
            if int(command_list[1]) > len(to_do_list):
                print("No such Task with number " + command_list[1] + " exists")
                return "error"
            return (command_list[0], int(command_list[1]))
        elif command.lower() == "tasks":
            return "tasks"
        elif command.lower() == "instructions":
            return "instructions"
        elif command.lower() == "save":
            return "save"
        else:
            return "error"

def readToDOListFile():
    
    file = Path("C:/users/user/desktop/do_not_delete/to_do_list.txt")
    if file.exists():
        with open(file,"r") as file:
            file_text = file.read()
            return eval(file_text)
    else:
        file_dir = Path("C:/users/user/desktop/do_not_delete")
        file_dir.mkdir()
        with open(file, "w") as to_do_list_file:
            to_do_list_file.write("[]")
        with open(file, "r") as to_do_list_file:
            file_text = to_do_list_file.read()
            return eval(file_text)

def saveToDoList(to_do_list):
    # for i in range(len(to_do_list)):
    #     to_do_list[i][1] = i + 1

    file = Path("C:/users/user/desktop/do_not_delete/to_do_list.txt")
    with file.open("w") as file:
        file.write(str(to_do_list))

def runProgram():
    command = ""
    while command != "exit":
        command = readInput()
        if command == "close":
            saveToDoList(to_do_list)
            print("Thanks for keeping track of your tasks with us, Bye")
            sys.exit()
        elif command == "save":
            saveToDoList(to_do_list)
            print("Your to-do-list has been saved")
        elif command == "error":
            print("There is an error somewhere in the command you typed. Please follow the instructions. Type instructions to see full list of instructions")
        elif command == "instructions":
            instructions()
        elif command == "tasks":
            if len(to_do_list) != 0:
                print("")
                for task in to_do_list:
                    if task[2]== "marked":
                        marked = "[Done☑]"
                    else:
                        marked = "" 
                    print(str(task[1]) + "- " + task[0] + " %s" % marked)
                print("")
            else:
               print("No task on the list currently")
        elif command[0] == "mark":
            to_do_list[command[1] - 1][2] = "marked"
            print(f"Task '{to_do_list[command[1] - 1] [0]}' has been marked as done")
        elif command[0] == 'remove':
            task = to_do_list[command[1] - 1]
            delete_permission = ""
            while delete_permission != "close":
                print("Are you sure you want to delete task '" + task[0] + "'")
                delete_permission = input("Type yes or no: ")
                if delete_permission.lower() == "yes":
                    to_do_list.remove(task)
                    print(f"Task '{task[0]}' has been removed from your to do list")
                    for i in range(len(to_do_list)):
                        to_do_list[i][1] = i + 1
                    break
                elif delete_permission.lower() == "no":
                    print("Okay, try again")
                    break
                else:
                    print("Only yes or no is allowed.")
        elif command[0] == "add":
            if to_do_list != []:
                task_number = to_do_list[-1][1] + 1
            else:
                task_number = 1
            to_do_list.append([command[1],task_number,""])
            # print(to_do_list)
            print(f"Task '{command[1]}' has been added to your to do list")
        sys.argv = []

to_do_list = readToDOListFile()
instructions()
runProgram()