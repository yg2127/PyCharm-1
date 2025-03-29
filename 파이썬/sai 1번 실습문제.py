import pandas as pd

student_dict_list = [{'이름':'Jake', '키':175, '성적':'A'}, {'이름':'Jay', '키':183, '성적':'B'}]

df = pd.DataFrame(student_dict_list)

def add_cm(value):
    return f"{value}cm"

df['키'] = df['키'].apply(add_cm)

print(df)