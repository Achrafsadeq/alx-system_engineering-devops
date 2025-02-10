#!/usr/bin/python3
"""
Script that exports TODO list information for all employees to JSON format
"""
import json
import requests


def export_all_tasks():
    """Export all employees' TODO list information to JSON file"""
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{base_url}/users").json()

    all_tasks = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        todos = requests.get(f"{base_url}/todos?userId={user_id}").json()

        user_tasks = []
        for todo in todos:
            user_tasks.append({
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            })
        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_tasks()
