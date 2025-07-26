import pandas as pd

df = pd.read_excel("Test.xlsx")

df.to_csv("Test.csv", index=False)

import xlrd
import csv

workbook = xlrd.open_workbook("Test.xlsx")
sheet = workbook.sheet_by_index(0)

with open("Test.csv", 'w', newline="") as csvfile:
writer = csv.writer(csvfile)
for row in range(sheet.nrows):
writer.writerow(sheet.row_values(row))

import openpyxl
import csv

workbook = openpyxl.load_workbook("Test.xlsx")
sheet = workbook.active

with open("Test.csv", 'w', newline="") as csvfile:
writer = csv.writer(csvfile)
for row in sheet.iter_rows(values_only=True):
writer.writerow(row)
