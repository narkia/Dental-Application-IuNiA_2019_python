import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
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
        con.execute("PRAGMA foreign_keys = 1")
        patient_id_local = []
        with con:

            cur1 = con.cursor()
            cur1.execute("SELECT id from patient_table_good3 WHERE firstname = ?", (firstname,))
            rows = cur1.fetchall()
            for id in rows:
                patient_id_local = id

            patient_id_local_val = patient_id_local[0]

            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS appointment_table_good7(appointment_id INTEGER NOT NULL PRIMARY KEY, firstname TEXT, lastname TEXT, appointment_day TEXT, start_hour TEXT, stop_hour TEXT, patient_id INTEGER NOT NULL, FOREIGN KEY (patient_id) REFERENCES patient_table_good3 (id) ON UPDATE CASCADE ON DELETE CASCADE)")
            cur.execute("INSERT INTO appointment_table_good7(firstname, lastname, appointment_day, start_hour, stop_hour, patient_id) values(?, ?, ?, ?, ?, ?)", (firstname, lastname, appointment_day, start_hour, stop_hour, patient_id_local_val))
        con.close()
        print ("un nou appointment *" + self.appointment_day + " " + self.start_hour + "* a fost adaugat")

    def print_appointment_database(self):

        con = sqlite.connect('test.db')

        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM appointment_table_good7')
            rows = cur.fetchall()
            print("continutul bazei de date *appointment_table_good6* este --> \n")
            for row in rows:
                print(row)
        con.close()