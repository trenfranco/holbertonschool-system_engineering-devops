#!/usr/bin/python3
"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""


if __name__ == "__main__":

    import json
    from sys import argv
    import requests

    empId = argv[1]
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(empId))
    name = response.json().get("name")

    res = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                       .format(empId))
    ttasks = 0
    dtasks = 0

    for tasks in res.json():
        ttasks += 1
        if tasks.get("completed"):
            dtasks += 1

    print("Employee {} is done with tasks ({}/{}):"
          .format(name, dtasks, ttasks))
    for tasks in res.json():
        if tasks.get("completed") and tasks.get("title"):
            print("\t {}".format(tasks.get('title')))
