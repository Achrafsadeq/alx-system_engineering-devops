#!/usr/bin/python3
"""
Script that exports TODO list information for a given employee ID to JSON format
"""
import json
import requests
import sys


def export_to_json(employee_id):
    """Export TODO list information to JSON file"""
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()
    username = user.get("username")

    tasks_list = []
    for todo in todos:
        tasks_list.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        })

    json_data = {str(employee_id): tasks_list}

    with open(f"{employee_id}.json", mode='w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    export_to_json(int(sys.argv[1]))
