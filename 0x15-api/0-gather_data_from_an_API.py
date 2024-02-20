#!/usr/bin/python3
""" Gets the employees completed TODO list"""
import requests
import sys

def get_todo_list_progress(employee_id):
    """
    gets the todo_list progress
    returns the completed and total list 
    """
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todo_list = response.json()
    name_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_name = name_response.json()
    # Get the total number of todo_list
    total_todo_list = len(todo_list)
    completed_inthe_list = [task for task in todo_list if task['completed']]

    return employee_name['name'], completed_inthe_list, total_todo_list


if __name__ == '__main__':
    employee_id = sys.argv[1]
    name, completed_todos, total_todos = get_todo_list_progress(employee_id)
    print(f"Employee {name} is done with tasks({len(completed_todos)}/{total_todos}):")
    for task in completed_todos:
        print(f"\t {task['title']}")