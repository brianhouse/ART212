#!/usr/bin/env python3

import yaml, sys, json

F  = 0      # non-existent
B_ = 80     # unsatisfactory - fails to fulfill the basic requirements
B  = 85     # satisfactory - functional / conceptually sound as expected
A_ = 90     # going places, but uneven
A  = 95     # a level of refinement and/or experimentation beyond the basic requirements

## sample student data
student = """
assignments:
    1: B
    2: B
    3: B
    4: B
presentation: A-
absences: 1
distractions: 1
"""

## load student data
print()
try:
    with open("students/" + sys.argv[1].split('.')[0] + '.yaml') as f:
        print(sys.argv[1].upper().split('.')[0])
        student = yaml.safe_load(f.read())
except IndexError:
    print('[student]')
    print()
    print('EXAMPLE')
    student = yaml.safe_load(student)
except Exception as e:
    print(e)
    exit()


## calculate grade on assignments
assignments = [globals()[value.replace('-', '_')] for value in student['assignments'].values()]
assignment_grade = sum(assignments) / (len(student['assignments']) * 100)
print(f"This project: {assignments[-1]}")
print(f"Projects to date: {(assignment_grade * 100)}")


## calculate grade on presentation
if 'presentation' in student:
    presentation = globals()[student['presentation'].replace('-', '_')]
    print(f"Presentation: {presentation}")
    presentation_grade = presentation / 100
    raw_grade = (assignment_grade * .9) + (presentation_grade * .1)
else:
    raw_grade = assignment_grade


"""
    absence -2.5%, 1 free
    distraction (late or social media use) -1.25%
    capped at -10%
"""
absence_factor = max((student['absences'] - 1), 0) * 0.025
absence_factor += student['distractions'] * 0.0125
absence_factor = min(absence_factor, .1)
print(f"Absences and distractions: {absence_factor * 100}")
final_grade = raw_grade - absence_factor
final_grade *= 100

print(f"Course: {final_grade}")
