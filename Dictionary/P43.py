# 43.	Given a JSON-like string of student details, parse it into a dictionary.
# Answer:
# Use json.loads to safely parse JSON input.

import json
s = input('Enter JSON string for student (e.g. {"name":"A","age":20}): ')
try:
    student = json.loads(s)
    print("Parsed dictionary:", student)
except Exception as e:
    print("Invalid JSON:", e)
