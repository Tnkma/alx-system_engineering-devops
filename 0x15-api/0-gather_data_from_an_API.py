#!/usr/bin/python3
""" Gets the employees completed TODO list"""
import requests
import sys


def list_progress(employee_id):

    """
    gets the todo_list progress
    returns the completed and total list
    """

    tod_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(tod_url)
    todo_list = response.json()

    name_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    name_response = requests.get(name_url)
    employee_name = name_response.json()

    # Get the total number of todo_list
    total_todo_list = len(todo_list)
    completed_list = [task for task in todo_list if task['completed']]

    return employee_name['name'], completed_list, total_todo_list


if __name__ == '__main__':
    employee_id = sys.argv[1]
    name, compl_todos, total_todos = list_progress(employee_id)
    dtask = len(compl_todos)
    print(f"Employee {name} is done with tasks({dtask}/{total_todos}):")
    for task in compl_todos:
        print(f"\t {task['title']}")
