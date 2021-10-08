#!/usr/bin/env python3

import sys, os, random, json

SIZE = 4

students = []

path = os.path.join(os.path.dirname(__file__), "students")
for filename in os.listdir(path):
    if filename.split('.')[-1] == "yaml":
        students.append(filename.split('.')[0])

random.shuffle(students)

groups = [students[i:i + SIZE] for i in range(0, len(students), SIZE)]

print(json.dumps(groups, indent=4))
