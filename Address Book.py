# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:40:45 2016

@author: Natalia Tucholska
"""

import os.path

save_path = 'C:/Users/Natalia Tucholska/Desktop/Python Projects/'

name_of_file = input("What is the name of the file: ")

completeName = os.path.join(save_path, name_of_file+".txt")   

file1 = open(completeName, 'w')

def new_contact():
    contact_name = input("Please enter contact name: ")
    file1.write("Name: " + contact_name + "         ")
    contact_address = input("Please enter contact address: ")
    file1.write("Address: " + contact_address + " \n")
    contact_work_phone = input("Please enter contact work phone: ")
    file1.write("Workphone: " + contact_work_phone + "         ")
    contact_cell_phone = input("Please enter contact cellphone: ")
    file1.write("Cellphone: " + contact_cell_phone + " \n")
    contact_email = input("Please enter contact email: ")
    file1.write("Contact Email: " + contact_email + "        ")
    contact_birthday = input("Please enter contact birthday: ")
    file1.write("Contact Birthday: " + contact_birthday + "       ")
    contact_notes = input("Please enter contact notes: ")
    file1.write("Contact Notes: " + contact_notes + "        ")
    file1.write("\n")
    file1.write("\n")
 
user_input = input("Would you like to add a new contact? (yes or no): ")

if user_input == "yes":
    new_contact()

user_input = input("Would you like to add another contact?: ")

while user_input == "yes":
    new_contact()
    user_input = input("Would you like to add another contact?: ")

file1.close() 