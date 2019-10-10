import Tkinter
from Tkinter import *
import Tkinter as tk
import tkMessageBox
from datetime import date
import os.path
import subprocess
import sqlite3 as sqlite
import uuid


class Appointment:

    def __init__(self, firstname, lastname, appointment_day, start_hour, stop_hour):
        self.firstname = firstname
        self.lastname = lastname
        self.appointment_day = appointment_day
        self.start_hour = start_hour
        self.stop_hour = stop_hour

    def add_appointment_in_database(self, firstname, lastname, appointment_day, start_hour, stop_hour):
        con = sqlite.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS appointment_table_good1(appointment_id INTEGER NOT NULL PRIMARY KEY, patient_id INTEGER NOT NULL, FOREIGN KEY (patient_id) REFERENCES patient_table_good3 (id), firstname TEXT, lastname TEXT, day DATE, start_hour TIME, stop hour TIME)")
            cur.execute("INSERT INTO appointment_table_good1(firstname, lastname, day, start_hour, stop hour) values(?, ?, ?, ?, ?)",
                        (firstname, lastname, appointment_day, start_hour, stop_hour))
        con.close()
        print ("un nou appointment *" + self.appointment_day + " " + self.start_hour + "* a fost adaugat")
