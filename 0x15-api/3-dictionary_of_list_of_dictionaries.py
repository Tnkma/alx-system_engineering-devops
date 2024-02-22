#!/usr/bin/python3
"""Gets the data from API and exports it to json"""
import json
import requests


def list_progress(employee_id):
    """A function to get the employee data"""
    tod_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(tod_url)
    todo_list = response.json()

    name_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    name_response = requests.get(name_url)
    employee_name = name_response.json()['username']

    completed_list = [task for task in todo_list if task['completed']]
    return employee_name, completed_list, todo_list


if __name__ == "__main__":
    all_employee_data = {}
    for employee_id in range(1, 11):
        username, completed, todo_list = list_progress(employee_id)
        user_tasks = [{"username": username, "task": task['title'],
                       "completed": task['completed']} for task in todo_list]
        all_employee_data[str(employee_id)] = user_tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_employee_data, file)
        # Use indent for pretty formatting
