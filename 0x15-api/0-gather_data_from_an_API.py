#!/usr/bin/python3
"""
Python script that retains information about an employee usind their id,
Retains information about an employee's TODO list.
"""
import requests
import sys


def main() -> None:
    """
    Main Function to execute the script
    """
    # Grab Employee Id as the 2nd argument
    employee_id = sys.argv[1]

    # Grab Employee Information
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )

    # Check Response
    if response.status_code == 200:
        # Grab Employee Information
        employee_info = response.json()
        employee_name = employee_info.get("name")
        # Grab Employee TODO List
        todo_list = requests.get(
            f"https://jsonplaceholder.typicode.com/todos"
        ).json()
        # Grab Employee TODO List
        employee_todo_list = [
            todo for todo in todo_list
            if todo.get("userId") == int(employee_id)
        ]
        completed_tasks = [
            todo for todo in employee_todo_list
            if todo.get("completed") is True
        ]
        tasks = len(employee_todo_list)
        completed = len(completed_tasks)
        # Print
        print(
            "Employee {} is done with tasks({}/{}):".format(
                employee_name,
                completed,
                tasks
            )
        )
        # Print completed task titles
        for task in completed_tasks:
            print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    # Run main script
    main()
