import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import date
import os.path
import subprocess
import sqlite3 as sqlite
import uuid


class Patient:

    def __init__(self, firstname, lastname, cnp, address_country, address_city, address_street, occupation):
        self.firstname = firstname
        self.lastname = lastname
        self.cnp = cnp
        self.address_country = address_country
        self.address_city = address_city
        self.address_street = address_street
        self.occupation = occupation

    #function with parameters because I use lambda: in main file - for button command
    def add_patient_in_database(self, firstname, lastname, cnp, address_country, address_city, address_street, occupation):
        con = sqlite.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS patient_table_good3(id INTEGER NOT NULL PRIMARY KEY, firstname TEXT, lastname TEXT, cnp TEXT, address_country TEXT, address_city TEXT, address_street TEXT, occupation TEXT)")
            cur.execute("INSERT INTO patient_table_good3(firstname, lastname, cnp, address_country, address_city, address_street, occupation) values(?, ?, ?, ?, ?, ?, ?)",
                        (firstname, lastname, cnp, address_country, address_city, address_street, occupation))
        con.close()
        print("un nou pacient *" + self.firstname + " " + self.lastname + "* a fost adaugat")


    def search_patient_in_database(self, input):
        patient_local_list = []
        con = sqlite.connect('test.db')
        with con:
            cur = con.cursor()
            #cur.execute("SELECT firstname, lastname from patient_table_good3 WHERE firstname LIKE ? OR lastname LIKE ?",(input, input)) #BUN
            #cur.execute("SELECT firstname, lastname from patient_table_good3 WHERE firstname.letter LIKE ? OR lastname.letter LIKE ?", (input, input))
            if(input is not ""):
                cur.execute("SELECT firstname, lastname from patient_table_good3 WHERE instr(firstname, ?) > 0 OR instr(lastname, ?) > 0",(input, input))
                rows = cur.fetchall()
                for patient_local in rows:
                    patient_local_list.append(patient_local[0] +" "+ patient_local[1])
        con.close()

        for item in patient_local_list:
            print(item)

        if not patient_local_list:
            print("nu s-a gasit nici un pacient care sa se numeasca ->", input)
        return patient_local_list
