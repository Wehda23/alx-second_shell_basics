#!/usr/bin/python3
"""
Python script that retains information about an employee usind their id,
Retains information about an employee's TODO list.
"""
import json
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
        employee_name = employee_info.get("username")
        # Grab Employee TODO List
        todo_list = requests.get(
            f"https://jsonplaceholder.typicode.com/todos"
        ).json()
        # Grab Employee TODO List
        employee_todo_list = [
            todo for todo in todo_list
            if todo.get("userId") == int(employee_id)
        ]
        # Reformat
        for todo in employee_todo_list:
            # Add username key
            todo['username'] = employee_name
            todo['task'] = todo['title']
            # remove keys
            todo.pop("title")
            todo.pop("userId")
            todo.pop("id")

        json_data = {
            f"{employee_id}": employee_todo_list,
        }
        # File name
        filename = f"{employee_id}.json"
        # Save to Json File
        with open(filename, "w") as json_file:
            # Save to json
            json.dump(json_data, json_file)


if __name__ == "__main__":
    # Run main script
    main()
