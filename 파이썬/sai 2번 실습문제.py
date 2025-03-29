import pandas as pd

students = [
    { "name" : "johanson", "age" : 23, "grade" : "B"},
    { "name" : "kelvin", "age" : 21, "grade" : "A"},
    { "name" : "smith", "age" : 22, "grade" : "F"},
    { "name" : "Jin", "age" : 20, "grade" : "A"},
    { "name" : "Chalie", "age" : 22, "grade" : "C"},
    { "name" : "Jackson", "age" : 21, "grade" : "B"},
    { "name" : "Michelle", "age" : 21, "grade" : "A"},
    { "name" : "Lisa", "age" : 24, "grade" : "F"}
]

df = pd.DataFrame(students)

grouped = df.groupby('grade')

for grade, group in grouped:
    print(f"{grade} : {len(group)}")
    print(group, "\n")