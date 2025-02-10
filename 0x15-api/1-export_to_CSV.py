#!/usr/bin/python3
"""
Script that exports TODO list information for a given employee ID to CSV format
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Export TODO list information to CSV file"""
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()
    username = user.get("username")

    with open(f"{employee_id}.csv", mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                employee_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    export_to_csv(int(sys.argv[1]))
