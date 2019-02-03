import csv,sqlite3
import tarfile
import os
#C:\Users\jtuch\Desktop\Person.csv
#Reads a csv input file given from the command line, this csv file is called person and is saved on the desktop
#The Csv format can be fixed with the tables pre created, because just created in an excel document. 
userinput = input('Enter the name of a file you want to read:')
myfile = open(userinput)
info = myfile.readlines()
print info
myfile.close()


#Connecting to a SQLite database and inserting the Person.csv file there
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

with open(userinput,'rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['col1'], i['col2']) for i in dr]

cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)

#Printing a summary as output 
results = cur.fetchall()
print(results)

con.commit()
con.close()

#Creates a full compressed tar file using Python 
def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname = os.path.basename(source_dir))


