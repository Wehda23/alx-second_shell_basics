#!/usr/bin/python3
"""
Python script that retains information about an employee usind their id,
Retains information about an employee's TODO list.
"""
import requests
import sys
import csv


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
        # File name
        filename = f"{employee_id}.csv"
        csv_data = []
        # Loop over employee's todo list
        for todo in employee_todo_list:
            csv_data.append(
                [
                    employee_id,
                    employee_name,
                    str(todo.get("completed")),
                    todo.get("title")
                ]
            )
        # Write file
        with open(filename, mode="w") as file:
            # write to file
            writer = csv.writer(
                file,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_ALL,
                lineterminator='\n'
            )
            for task in csv_data:
                writer.writerow(
                    task
                )


if __name__ == "__main__":
    # Run main script
    main()
