import sys 
import difflib

def check(refFile, sourceFile):
    with open(refFile) as file_1:
         with open(sourceFile) as file_2:
             file1_data = file_1.read()
             print file1_data
             
             file2_data = file_2.read()
             print file2_data
             s = difflib.SequenceMatcher(None,file1_data, file2_data) 
             s1 = s.ratio()*100
             msg = "This is the rate of plagarism"
             msg += str(s1) #plagiarism detectedzz
             
             return msg 
