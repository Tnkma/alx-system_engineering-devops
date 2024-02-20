#!/usr/bin/python3
""" Gets the employees completed TODO list"""
import csv
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
    # total_todo_list = len(todo_list)
    completed_list = [task for task in todo_list if task['completed']]
    return employee_name['username'], completed_list, todo_list


if __name__ == '__main__':
    e_id = sys.argv[1]
    name, compl_todos, total_todos = list_progress(e_id)
    csv_file = f'{e_id}.csv'
    # print(f"Employee {name} is done with tasks({dtask}/{total_todos}):")
    with open(csv_file, 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in total_todos:
            title = task['title']
            status = 'True' if task['completed'] else 'False'
            row = [e_id, name, status, title]
            writer.writerow(row)
