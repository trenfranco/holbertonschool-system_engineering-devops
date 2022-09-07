#!/usr/bin/python3
"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""


import csv
import json
import requests
from sys import argv

if __name__ == "__main__":

    filename = "todo_all_employees.json"

    # response is dict type
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    # res is list type when passed parameters
    res = requests.get("https://jsonplaceholder.typicode.com/todos")
    res = res.json()
    response = response.json()

    big_dict = {}
    dic = {}
    list_dicts = []

    for user in response:
        list_dicts = []
        for i in res:
            dic['username'] = user['username']
            dic['task'] = i['title']
            dic['completed'] = i['completed']
            list_dicts.append(dic)
        big_dict[user['id']] = list_dicts

    with open(filename, 'w') as f:
        f.write(json.dumps(big_dict))
    f.close()
