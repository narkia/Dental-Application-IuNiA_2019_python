
import sqlite3 as sqlite


class Consult:

    def __init__(self):
        pass

    def add_consult_in_database(self):
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
            cur.execute("CREATE TABLE IF NOT EXISTS consult_table(consult_id INTEGER NOT NULL PRIMARY KEY, patient_id INTEGER NOT NULL, appointment_id INTEGER NOT NULL, FOREIGN KEY (patient_id) REFERENCES patient_table_good3 (id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY (appointment_id) REFERENCES appointment_table_good7(id) ON UPDATE CASCADE ON DELETE CASCADE)")
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