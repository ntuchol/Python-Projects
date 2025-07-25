import pandas as pd

data = pd.DataFrame({
    'Column1': [1, 2, None, 4],
    'Column2': ['A', None, None, 'D']
})

blank_rows = data.isnull().all(axis=1)

data.loc[blank_rows] = ['Placeholder'] * len(data.columns)

print(data)

data = [
    [1, 'A'],
    [None, None],
    [3, 'C'],
    [None, None]
]

for row in data:
    if all(cell is None for cell in row):
        row[:] = ['Inverted', 'Row']

print(data)

data = [row for row in data if not all(cell is None for cell in row)]

print(data)
