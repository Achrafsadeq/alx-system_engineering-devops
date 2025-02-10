#!/usr/bin/python3
"""
Script that retrieves TODO list progress for a given employee ID using REST API
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Get TODO list progress for specified employee"""
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()

    total_tasks = len(todos)
    done_tasks = len([task for task in todos if task.get("completed")])
    employee_name = user.get("name")

    # Display progress with exact formatting
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

    # Display completed tasks
    for todo in todos:
        if todo.get("completed"):
            print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    get_employee_todo_progress(int(sys.argv[1]))
