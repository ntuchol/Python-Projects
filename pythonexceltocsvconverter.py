import pandas as pd

# Read the Excel file
df = pd.read_excel("Test.xlsx")

# Convert the DataFrame to a CSV file
df.to_csv("Test.csv", index=False)

import xlrd
import csv

# Open the Excel file
workbook = xlrd.open_workbook("Test.xlsx")
sheet = workbook.sheet_by_index(0)

# Create a CSV writer object
with open("Test.csv", 'w', newline="") as csvfile:
writer = csv.writer(csvfile)
for row in range(sheet.nrows):
writer.writerow(sheet.row_values(row))

import openpyxl
import csv

# Load the workbook and select the active sheet
workbook = openpyxl.load_workbook("Test.xlsx")
sheet = workbook.active

# Create a CSV writer object
with open("Test.csv", 'w', newline="") as csvfile:
writer = csv.writer(csvfile)
for row in sheet.iter_rows(values_only=True):
writer.writerow(row)