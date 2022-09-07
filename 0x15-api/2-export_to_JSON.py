#!/usr/bin/python3
"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""


import csv
import json
import requests
from sys import argv

if __name__ == "__main__":

    empId = argv[1]
    filename = "{}.json".format(empId)

    # response is dict type
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(empId))
    username = response.json().get("username")

    # res is list type when passed parameters
    res = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                       .format(empId))
    res = res.json()
    response = response.json()

    big_dict = {}
    listof_dicts = []

    for i in res:
        dic = {}
        dic["task"] = i["title"]
        dic["completed"] = i["completed"]
        dic["username"] = username
        listof_dicts.append(dic)

    big_dict[empId] = listof_dicts

    with open(filename, 'w') as f:
        f.write(json.dumps(big_dict))
    f.close()
