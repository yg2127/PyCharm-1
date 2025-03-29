import pandas as pd

data = {
    'Fruit': ['Apple', 'Banana', 'Cherry'],
    'Amount': [3, 2, 10],
    'Price': [3000, 1500, 7000]
}

df = pd.DataFrame(data)

print(df)