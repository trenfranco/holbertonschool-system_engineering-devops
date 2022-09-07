#!/usr/bin/python3
"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""


import csv
import json
import requests
from sys import argv

if __name__ == "__main__":

    empId = argv[1]
    filename = "{}.csv".format(empId)

    # response is dict type
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(empId))
    username = response.json().get("username")

    # res is list type when passed parameters
    res = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                       .format(empId))
    res = res.json()
    response = response.json()

    with open(filename, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for fil in res:
            row = [empId, username, fil['completed'], fil['title']]
            writer.writerow(row)
        f.close()
