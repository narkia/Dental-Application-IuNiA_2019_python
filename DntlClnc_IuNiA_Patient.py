import Tkinter
from Tkinter import *
import Tkinter as tk
import tkMessageBox
from datetime import date
import os.path
import subprocess
import sqlite3 as sqlite
import uuid


class Patient:

    def __init__(self, firstname, lastname, birthdate, cnp, address_country, address_city, address_street, occupation):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.cnp = cnp
        self.address_country = address_country
        self.address_city = address_city
        self.address_street = address_street
        self.occupation = occupation

    #function with parameters because I use lambda: in main file - for button command
    def add_patient_in_database(self, firstname, lastname, birthdate, cnp, address_country, address_city, address_street, occupation):
        con = sqlite.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS patient_table_good2(id INTEGER NOT NULL PRIMARY KEY, firstname TEXT, lastname TEXT, birthdate DATE, cnp TEXT, address_country TEXT, address_city TEXT, address_street TEXT, occupation TEXT)")
            cur.execute("INSERT INTO patient_table_good2(firstname, lastname, birthdate, cnp, address_country, address_city, address_street, occupation) values(?, ?, ?, ?, ?, ?, ?, ?)",
                        (firstname, lastname, birthdate, cnp, address_country, address_city, address_street, occupation))
                        #(self.firstname, self.lastname, self.birthdate, self.cnp, self.address_country, self.address_city, self.address_street, self.occupation))
        con.close()
        print ("un nou pacient *" + self.firstname + " " + self.lastname + "* a fost adaugat")
        #asa da