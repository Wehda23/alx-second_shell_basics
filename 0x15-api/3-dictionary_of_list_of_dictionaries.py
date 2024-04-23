#!/usr/bin/python3
"""
Python script that retains information about an employee usind their id,
Retains information about an employee's TODO list.
"""
import json
import requests
import sys


def employee_information(username: str, employee_id: int, todos: list) -> object:
    """
    Function that takes in employee id and returns data about employee.

    Args:
        - username (str): User name of an employee.
        - employee_id (int): Id of an existing employee.
        - todos (list): List of TODOs for an employee.

    Returns:
        - Python Dictionary that contains employee information.
    """
    # Grab Employee TODO List
    employee_todo_list = [
        todo for todo in todos
        if todo.get("userId") == int(employee_id)
    ]
    # Reformat
    for todo in employee_todo_list:
        # Add username key
        todo['username'] = username
        todo['task'] = todo['title']
        # remove keys
        todo.pop("title")
        todo.pop("userId")
        todo.pop("id")
    # Return Dictionary with employee id as key.
    return {employee_id: employee_todo_list}


def main() -> None:
    """
    Main Function to execute the script
    """
    # Grab Employee TODO List
    todo_list = requests.get(
        f"https://jsonplaceholder.typicode.com/todos"
    ).json()
    # Declare an empty list
    json_data = {}
    # Starting id
    employee_id = 0
    # Loop over employees
    while True:
        # Grab Employee ID
        employee_id += 1
        # Grab Employee Information
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        )
        # Grab Employee Information
        employee_info = response.json()
        # Stop Scraping in case employee info starts returning empty dicts.
        if not employee_info:
            break;
        employee_name = employee_info.get("username")
        # Get employee infromation
        data = employee_information(
            employee_name,
            employee_id,
            todo_list
        )
        # Get the data
        json_data = {**json_data, **data}

    # File name
    filename = f"todo_all_employees.json"
    # Save to Json File
    with open(filename, "w") as json_file:
        # Save to json
        json.dump(json_data, json_file)


if __name__ == "__main__":
    # Run main script
    main()
