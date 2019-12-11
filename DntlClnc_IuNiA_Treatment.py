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
            cur.execute("INSERT INTO treatment_table_good3(treatment_name, treatment_cost) values(?, ?)",(treatment_name, treatment_cost))
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

    def __init__(self, treatmentPlan_name, treatmentPlan_step_1, treatmentPlan_step_2, treatmentPlan_step_3, treatmentPlan_step_4, treatmentPlan_step_5, treatmentPlan_step_6, treatmentPlan_step_7, treatmentPlan_step_8, treatmentPlan_step_9, treatmentPlan_step_10, treatmentPlan_duration, treatmentPlan_cost):
        self.treatmentPlan_name = treatmentPlan_name
        self.treatmentPlan_steps = treatmentPlan_step_1
        self.treatmentPlan_steps = treatmentPlan_step_2
        self.treatmentPlan_steps = treatmentPlan_step_3
        self.treatmentPlan_steps = treatmentPlan_step_4
        self.treatmentPlan_steps = treatmentPlan_step_5
        self.treatmentPlan_steps = treatmentPlan_step_6
        self.treatmentPlan_steps = treatmentPlan_step_7
        self.treatmentPlan_steps = treatmentPlan_step_8
        self.treatmentPlan_steps = treatmentPlan_step_9
        self.treatmentPlan_steps = treatmentPlan_step_10
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

    def add_treatmentPlan_in_database(self, treatmentPlan_name, treatmentPlan_step_1, treatmentPlan_step_2, treatmentPlan_step_3, treatmentPlan_step_4, treatmentPlan_step_5, treatmentPlan_step_6, treatmentPlan_step_7, treatmentPlan_step_8, treatmentPlan_step_9, treatmentPlan_step_10, treatmentPlan_duration, treatmentPlan_cost):
        con = sqlite.connect('test.db')
        flag = 0
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS treatmentPlan_table(treatmentPlan_id INTEGER NOT NULL PRIMARY KEY, treatment_name TEXT, treatmentPlan_step_1 TEXT, treatmentPlan_step_2 TEXT, treatmentPlan_step_3 TEXT, treatmentPlan_step_4 TEXT, treatmentPlan_step_5 TEXT, treatmentPlan_step_6 TEXT, treatmentPlan_step_7 TEXT, treatmentPlan_step_8 TEXT, treatmentPlan_step_9 TEXT, treatmentPlan_step_10 TEXT, treatmentPlan_duration INTEGER, treatmentPlan_cost INTEGER)")
            cur.execute("INSERT INTO treatmentPlan_table(treatmentPlan_id, treatment_name, treatmentPlan_step_1, treatmentPlan_step_2, treatmentPlan_step_3, treatmentPlan_step_4, treatmentPlan_step_5, treatmentPlan_step_6, treatmentPlan_step_7, treatmentPlan_step_8, treatmentPlan_step_9, treatmentPlan_step_10, treatmentPlan_duration INTEGER, treatmentPlan_cost INTEGER) values(?, ?)",
                        (treatmentPlan_name, treatmentPlan_step_1, treatmentPlan_step_2, treatmentPlan_step_3, treatmentPlan_step_4, treatmentPlan_step_5, treatmentPlan_step_6, treatmentPlan_step_7, treatmentPlan_step_8, treatmentPlan_step_9, treatmentPlan_step_10, treatmentPlan_duration, treatmentPlan_cost))
        con.close()


    def print_treatmentPlan_database(self):

        con = sqlite.connect('test.db')

        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM treatmentPlan_table')
            rows = cur.fetchall()
            print("continutul bazei de date *treatmentPlan_table* este --> \n")
            for row in rows:
                print(row)
        con.close()