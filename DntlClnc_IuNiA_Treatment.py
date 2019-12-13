import sqlite3 as sqlite


class Treatment:

    def __init__(self, treatment_name, treatment_cost):
        self.treatment_name = treatment_name
        self.treatment_cost = treatment_cost

    def add_treatment_in_database(self, treatment_name, treatment_cost):
        con = sqlite.connect('test.db')
        flag = 0
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS treatment_table_good3(id INTEGER NOT NULL PRIMARY KEY, treatment_name TEXT, treatment_cost INT)")
            cur.execute("INSERT INTO treatment_table_good3(treatment_name, treatment_cost) values(?, ?)", (treatment_name, treatment_cost))
        con.close()


    def print_treatment_database(self):

        con = sqlite.connect('test.db')

        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM treatment_table_good3')
            rows = cur.fetchall()
            print("continutul bazei de date *treatment_table_good3* este --> \n")
            for row in rows:
                print(row)
        con.close()


class TreatmentPlan:

    def __init__(self, treatmentPlan_name, treatmentPlan_step_1, treatmentPlan_step_1_nr, treatmentPlan_step_2, treatmentPlan_step_2_nr, treatmentPlan_step_3, treatmentPlan_step_3_nr, treatmentPlan_step_4, treatmentPlan_step_4_nr, treatmentPlan_step_5, treatmentPlan_step_5_nr, treatmentPlan_step_6, treatmentPlan_step_6_nr, treatmentPlan_step_7, treatmentPlan_step_7_nr, treatmentPlan_step_8, treatmentPlan_step_8_nr, treatmentPlan_step_9, treatmentPlan_step_9_nr, treatmentPlan_step_10, treatmentPlan_step_10_nr, treatmentPlan_duration, treatmentPlan_cost):
        self.treatmentPlan_name = treatmentPlan_name
        self.treatmentPlan_step_1 = treatmentPlan_step_1
        self.treatmentPlan_step_2 = treatmentPlan_step_2
        self.treatmentPlan_step_3 = treatmentPlan_step_3
        self.treatmentPlan_step_4 = treatmentPlan_step_4
        self.treatmentPlan_step_5 = treatmentPlan_step_5
        self.treatmentPlan_step_6 = treatmentPlan_step_6
        self.treatmentPlan_step_7 = treatmentPlan_step_7
        self.treatmentPlan_step_8 = treatmentPlan_step_8
        self.treatmentPlan_step_9 = treatmentPlan_step_9
        self.treatmentPlan_step_10 = treatmentPlan_step_10
        self.treatmentPlan_step_1_nr = treatmentPlan_step_1_nr
        self.treatmentPlan_step_1_nr = treatmentPlan_step_2_nr
        self.treatmentPlan_step_1_nr = treatmentPlan_step_3_nr
        self.treatmentPlan_step_1_nr = treatmentPlan_step_4_nr
        self.treatmentPlan_step_1_nr = treatmentPlan_step_5_nr
        self.treatmentPlan_step_1_nr = treatmentPlan_step_6_nr
        self.treatmentPlan_step_1_nr = treatmentPlan_step_7_nr
        self.treatmentPlan_step_1_nr = treatmentPlan_step_8_nr
        self.treatmentPlan_step_1_nr = treatmentPlan_step_9_nr
        self.treatmentPlan_step_1_nr = treatmentPlan_step_10_nr
        self.treatmentPlan_duration = treatmentPlan_duration
        self.treatmentPlan_cost = treatmentPlan_cost

    #(1, 'implant', 4000)
    #(2, 'extractie', 200)
    #(3, 'obturatie', 500)
    #(4, 'tratament pe canal', 1000)
    #(5, 'detartraj', 200)
    #(6, 'igienizare', 200)
    #(7, 'periaj profesional', 230)
    #(8, 'tratament ortodontic', 3000)
    #(9, 'tratament protetic', 2000)
    #(10, 'taiere varf radacina', 500)

    def add_treatmentPlan_in_database(self, patientname, treatmentPlan_name, treatmentPlan_step_1, treatmentPlan_step_1_nr, treatmentPlan_step_2, treatmentPlan_step_2_nr, treatmentPlan_step_3, treatmentPlan_step_3_nr, treatmentPlan_step_4, treatmentPlan_step_4_nr, treatmentPlan_step_5, treatmentPlan_step_5_nr, treatmentPlan_step_6, treatmentPlan_step_6_nr, treatmentPlan_step_7, treatmentPlan_step_7_nr, treatmentPlan_step_8, treatmentPlan_step_8_nr, treatmentPlan_step_9, treatmentPlan_step_9_nr, treatmentPlan_step_10, treatmentPlan_step_10_nr, treatmentPlan_duration, treatmentPlan_cost):

        patient_id_local_val = 0
        treatmentPlan_name_local_list = []
        patient_name_list = []
        patient_name_list = patientname.split()
        patient_firstname = patient_name_list[0]
        patient_lastname = patient_name_list[1]
        treatmentPlan_name_local_list = treatmentPlan_name.split()
        treatmentPlan_name_local = str(treatmentPlan_name_local_list[0] + treatmentPlan_name_local_list[1])
        print(treatmentPlan_name_local)

        con = sqlite.connect('test.db')
        con.execute("PRAGMA foreign_keys = 1")
        patient_id_local = []
        with con:
            cur = con.cursor()

            cur.execute("SELECT id from patient_table_good3 WHERE firstname=? AND lastname=?", (patient_firstname, patient_lastname))
            rows = cur.fetchall()
            for id in rows:
                patient_id_local_val = id[0]

            print(type(patient_id_local_val))

            cur.execute("SELECT id from treatment_table_good3 WHERE treatment_name=?", (treatmentPlan_step_1,))
            rows = cur.fetchall()
            for id in rows:
                treatment_name_local_id = id[0]

            cur.execute("CREATE TABLE IF NOT EXISTS treatmentPlan_table14(treatmentPlan_id INTEGER NOT NULL PRIMARY KEY, treatmentPlan_name TEXT,"
                        "treatmentPlan_duration INTEGER, treatmentPlan_cost INTEGER,"
                        "treatmentPlan_step_1 INTEGER,"
                        "treatmentPlan_step_1_nr INTEGER,"
                        "treatmentPlan_step_2 INTEGER,"
                        "treatmentPlan_step_2_nr INTEGER,"
                        "treatmentPlan_step_3 INTEGER,"
                        "treatmentPlan_step_3_nr INTEGER,"
                        "treatmentPlan_step_4 INTEGER,  treatmentPlan_step_4_nr INTEGER,"
                        "treatmentPlan_step_5 INTEGER, treatmentPlan_step_5_nr INTEGER,"
                        "treatmentPlan_step_6 INTEGER, treatmentPlan_step_6_nr INTEGER,"
                        "treatmentPlan_step_7 INTEGER, treatmentPlan_step_7_nr INTEGER,"
                        "treatmentPlan_step_8 INTEGER, treatmentPlan_step_8_nr INTEGER,"
                        "treatmentPlan_step_9 INTEGER, treatmentPlan_step_9_nr INTEGER,"
                        "treatmentPlan_step_10 INTEGER, treatmentPlan_step_10_nr INTEGER,"
                        "patient_id INTEGER,"
                        "FOREIGN KEY (patient_id) REFERENCES patient_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                        "FOREIGN KEY (treatmentPlan_step_1) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                        #"FOREIGN KEY (treatmentPlan_step_2) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE"
                        #"FOREIGN KEY (treatmentPlan_step_3) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE"
                        # "FOREIGN KEY (treatmentPlan_step_2) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                        # "FOREIGN KEY (treatmentPlan_step_3) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                        # "FOREIGN KEY (treatmentPlan_step_4) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                        # "FOREIGN KEY (treatmentPlan_step_5) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                        # "FOREIGN KEY (treatmentPlan_step_6) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                        # "FOREIGN KEY (treatmentPlan_step_7) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                        # "FOREIGN KEY (treatmentPlan_step_8) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                        # "FOREIGN KEY (treatmentPlan_step_9) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                        # "FOREIGN KEY (treatmentPlan_step_10) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                        ")")

            # "FOREIGN KEY (treatmentPlan_step_1) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
            # "FOREIGN KEY (treatmentPlan_step_2) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
            # "FOREIGN KEY (treatmentPlan_step_3) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
            # "FOREIGN KEY (treatmentPlan_step_4) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
            # "FOREIGN KEY (treatmentPlan_step_5) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
            # "FOREIGN KEY (treatmentPlan_step_6) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
            # "FOREIGN KEY (treatmentPlan_step_7) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
            # "FOREIGN KEY (treatmentPlan_step_8) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
            # "FOREIGN KEY (treatmentPlan_step_9) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"
            # "FOREIGN KEY (treatmentPlan_step_10) REFERENCES treatment_table_good3(id) ON UPDATE CASCADE ON DELETE CASCADE,"

            cur.execute("INSERT INTO treatmentPlan_table14(treatmentPlan_name, treatmentPlan_duration, treatmentPlan_cost,"
                        " treatmentPlan_step_1, treatmentPlan_step_1_nr, treatmentPlan_step_2, treatmentPlan_step_2_nr, treatmentPlan_step_3, treatmentPlan_step_3_nr,"
                        " treatmentPlan_step_4, treatmentPlan_step_4_nr, treatmentPlan_step_5, treatmentPlan_step_5_nr, treatmentPlan_step_6, treatmentPlan_step_6_nr,"
                        " treatmentPlan_step_7, treatmentPlan_step_7_nr, treatmentPlan_step_8, treatmentPlan_step_8_nr, treatmentPlan_step_9, treatmentPlan_step_9_nr,"
                        " treatmentPlan_step_10, treatmentPlan_step_10_nr, patient_id) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        ("un plan", treatmentPlan_duration, treatmentPlan_cost,
                         treatment_name_local_id, treatmentPlan_step_1_nr, treatmentPlan_step_2,treatmentPlan_step_2_nr,
                         treatmentPlan_step_3, treatmentPlan_step_3_nr, treatmentPlan_step_4, treatmentPlan_step_4_nr,
                         treatmentPlan_step_5, treatmentPlan_step_5_nr, treatmentPlan_step_6, treatmentPlan_step_6_nr,
                         treatmentPlan_step_7, treatmentPlan_step_7_nr, treatmentPlan_step_8, treatmentPlan_step_8_nr,
                         treatmentPlan_step_9, treatmentPlan_step_9_nr,
                         treatmentPlan_step_10, treatmentPlan_step_10_nr, patient_id_local_val))
        con.close()


    def print_treatmentPlan_database(self):

        con = sqlite.connect('test.db')

        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM treatmentPlan_table14')
            rows = cur.fetchall()
            print("continutul bazei de date *treatmentPlan_table* este --> \n")
            for row in rows:
                print(row)
        con.close()