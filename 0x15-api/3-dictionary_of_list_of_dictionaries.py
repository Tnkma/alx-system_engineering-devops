#!/usr/bin/python3
" Gets the data from API and export it to json"
import json
import requests
import sys


def list_progress(employee_id):
    " A function to get the employee data"

    tod_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(tod_url)
    todo_list = response.json()

    name_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    name_response = requests.get(name_url)
    employee_name = name_response.json()

    completed_list = [task for task in todo_list if task['completed']]
    return employee_name['username'], completed_list, todo_list


if __name__ == "__main__":
    c_args = sys.argv[1]
    username, completed, todo_list = list_progress(c_args)

    # json_file = f'{c_args}.json'
    data = {
        c_args: [
            {"username": username, "task": task['title'],
             "completed": task['completed']}
            for task in todo_list
        ]
    }

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
        # Use indent for pretty formatting
