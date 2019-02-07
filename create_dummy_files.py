import os
from random import randint

number_of_people = 14
min_statements = 5
max_statements = 10

base_folder = 'test_statements'
for i in range(1, number_of_people + 1):
    c = chr(ord('A') + i - 1)
    fileName = f"person_{c}.txt"
    print(f"{i}: {fileName}")
    with open(os.path.join(base_folder, fileName), 'w') as f:
        for j in range(1, randint(min_statements + 1, max_statements + 1)):
            f.write(f"true statement {c}{j}\n")
