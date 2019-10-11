from Tkinter import *
import ttk
import Tkinter as tk
import tkMessageBox
from datetime import date
import os.path
import subprocess
from DntlClnc_IuNiA_Login import Login
from DntlClnc_IuNiA_Patient import Patient
from DntlClnc_IuNiA_Appointment import Appointment
import sqlite3 as sqlite

#import matplotlib.pyplot as plt
#from matplotlib.collections import EventCollection
#import numpy as np

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.wm_title("Application dntlclnc")
        self.switch_frame(NoteBook)


    # controller function
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def all_children(self):
        _list = self.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        return _list


# sub-root to contain the Notebook frame and a controller function to switch the tabs within the notebook
class NoteBook(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self._notebook = ttk.Notebook()
        self._tab0 = Tab_Login(self._notebook)
        self._tab1 = Tab_Main(self._notebook)
        self._tab2 = Tab_Patient_fake(self._notebook)
        self._tab3 = Tab_Appointment(self._notebook)
        self._tab4 = Tab_Statistic(self._notebook)
        self._tab5 = Tab_Logout(self._notebook)
        self._notebook.add(self._tab0, text="Login Window")
        self._notebook.add(self._tab1, text="Main Window")
        self._notebook.add(self._tab2, text="Patient Window")
        self._notebook.add(self._tab3, text="Appointment Window")
        self._notebook.add(self._tab4, text="Statistics Window")
        self._notebook.add(self._tab5, text="Logout Window")
        self._notebook.tab(1, state="disabled")
        self._notebook.tab(2, state="disabled")
        self._notebook.tab(3, state="disabled")
        self._notebook.tab(4, state="disabled")
        self._notebook.tab(5, state="disabled")
        self._notebook.pack()


    # controller function
    #def switch_tab1(self, frame_class):
    #    new_frame = frame_class(self._notebook)
    #    self._tab1.destroy()
    #   self._tab1 = new_frame


    def login_success_action(self):
        self.destroy()
        print("login efectuat cu succes, am creat o noua clasa Notebook_real cu taburi")


    def log_out_success_action(self):
        self.destroy()
        print("logout efectuat cu succes, am creat o noua clasa Notebook cu taburi")


# sub-root to contain the Notebook frame and a controller function to switch the tabs within the notebook
class NoteBook_real(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self._notebook = ttk.Notebook()
        self._tab0 = Tab_Login(self._notebook)
        self._tab1 = Tab_Main(self._notebook)
        self._tab2 = Tab_Patient(self._notebook)
        self._tab3 = Tab_Appointment(self._notebook)
        self._tab4 = Tab_Statistic(self._notebook)
        self._tab5 = Tab_Logout(self._notebook)
        self._notebook.add(self._tab0, text="Login Window")
        self._notebook.add(self._tab1, text="Main Window")
        self._notebook.add(self._tab2, text="Patient Window")
        self._notebook.add(self._tab3, text="Appointment Window")
        self._notebook.add(self._tab4, text="Statistics Window")
        self._notebook.add(self._tab5, text="Logout Window")
        self._notebook.tab(0, state="disabled")
        self._notebook.pack()

    # controller function
    def switch_tab1(self, frame_class):
        new_frame = frame_class(self._notebook)
        self._tab1.destroy()
        self._tab1 = new_frame

# Notebook - Tab 0
class Tab_Login(Frame):

    dictionar_users_and_passwords = {}
    dictionar_users_and_passwords_and_dates_of_account_creation = {}

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text="this is login tab")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self._label_1 = tk.Label(self, text="Enter Username").grid(row=0)
        self._label_2 = tk.Label(self, text="Enter Password").grid(row=1)
        self._textbox_1 = tk.Entry(self, width=40)
        self._textbox_2 = tk.Entry(self, width=40)
        self._textbox_1.grid(row=0, column=1)
        self._textbox_2.grid(row=1, column=1)
        self._textbox_1.config(state=NORMAL)
        self._textbox_2.config(state=NORMAL)
        self._button_login = tk.Button(self, text="Login", command=self.func_initial_login, bg="#E3F6CE", fg="blue")
        self._button_login.grid(row=2, column=1)
        self._button_signup = tk.Button(self, text="Sign Up", command=self.func_signup_login, bg="#E3F6CE")
        self._button_signup.grid(row=0, column=3)
#        self.label.pack()


    counter_login_tries = 0


    def func_initial_login(self):
        log = Login(Entry.get(self._textbox_1), Entry.get(self._textbox_2))
        return_database_accounts_exists = log.read_file_user_pass(self.dictionar_users_and_passwords, self.dictionar_users_and_passwords_and_dates_of_account_creation)#

        if return_database_accounts_exists == 1:
            return_check = log.check(Entry.get(self._textbox_1), Entry.get(self._textbox_2), self.dictionar_users_and_passwords)
            log.check_password_too_old(Entry.get(self._textbox_1), Entry.get(self._textbox_2), self.dictionar_users_and_passwords, self.dictionar_users_and_passwords_and_dates_of_account_creation)
            if return_check == 1:
                old_frame = NoteBook(self)
                NoteBook.login_success_action(old_frame)
                widget_list = app.all_children()
                for item in widget_list:
                    item.pack_forget()
                app.switch_frame(NoteBook_real)

            else:
                print "Login failed!!"
                if self.counter_login_tries == 3:
                    self._textbox_1.delete(0, END)
                    self._textbox_2.delete(0, END)
                    self._textbox_1.insert(1, "error")
                    self._textbox_2.insert(1, "error")
                    tkMessageBox.showwarning("Warning", "Login Failed!! Au trecut 3 incercari..")
                else:
                    self.counter_login_tries += 1
        else:
           tkMessageBox.showerror("Eroare", "Nu exista nici un cont in database. Sign Up first!!")


    def func_signup_login(self):
        app_signup_initial = GuiSignUpWindow()
        app_signup_initial.mainloop()




# Notebook - Tab 1
class Tab_Main(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self._frame = None
        self.switch_frame(Tab1_Frame1)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# first frame for Tab1
class Tab1_Frame1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text="this is a test - one")
        # button object with command to replace the frame
        self.button = Button(self, text="Change it!", command=lambda: master.switch_frame(Tab1_Frame2))
        self.label.pack()
        self.button.pack()


# second frame for Tab1
class Tab1_Frame2(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text="it has been changed!")
        # and another button to change it back to the previous frame
        self.button = Button(self, text="Change it back!", command=lambda: master.switch_frame(Tab1_Frame1))
        self.label.pack()
        self.button.pack()


# Notebook - Tab 2
class Tab_Patient_fake(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)


# Notebook - Tab 2
class Tab_Patient(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self._label_1 = Label(self, text="Enter Firstname").grid(row=0)
        self._label_2 = Label(self, text="Enter Lastname").grid(row=1)
        self._label_2 = Label(self, text="Enter CNP").grid(row=2)
        self._label_2 = Label(self, text="Enter Country").grid(row=3)
        self._label_2 = Label(self, text="Enter City").grid(row=4)
        self._label_2 = Label(self, text="Enter Street").grid(row=5)
        self._label_2 = Label(self, text="Enter Occupation").grid(row=6)
        self._textbox_firstname_patient = tk.Entry(self, width=40)
        self._textbox_lastname_patient = tk.Entry(self, width=40)
        self._textbox_cnp_patient = tk.Entry(self, width=40)
        self._textbox_country_patient = tk.Entry(self, width=40)
        self._textbox_city_patient = tk.Entry(self, width=40)
        self._textbox_street_patient = tk.Entry(self, width=40)
        self._textbox_occupation_patient = tk.Entry(self, width=40)
        self._textbox_firstname_patient.grid(row=0, column=1)
        self._textbox_lastname_patient.grid(row=1, column=1)
        self._textbox_cnp_patient.grid(row=2, column=1)
        self._textbox_country_patient.grid(row=3, column=1)
        self._textbox_city_patient.grid(row=4, column=1)
        self._textbox_street_patient.grid(row=5, column=1)
        self._textbox_occupation_patient.grid(row=6, column=1)
        patient_new = Patient("", "", "", "", "", "", "")
        self._button_add_patient = Button(self, text="Add patient", command=lambda: patient_new.add_patient_in_database(Entry.get(self._textbox_firstname_patient), Entry.get(self._textbox_lastname_patient), Entry.get(self._textbox_cnp_patient), Entry.get(self._textbox_country_patient), Entry.get(self._textbox_city_patient), Entry.get(self._textbox_street_patient), Entry.get(self._textbox_occupation_patient)), bg="#E3F6CE", fg="blue")
        self._button_add_patient.grid(row=7, column=1)
        self._button_delete_all_patients = Button(self, text="Delete All Patients", command=self.delete_all_patients_in_database, bg="#E3F6CE", fg="blue")
        self._button_delete_all_patients.grid(row=1, column=2)
        self._button_add_10_random_patients = Button(self, text="Add 10 Random Patients", command=self.add_10_random_patients_in_database, bg="#E3F6CE", fg="blue")
        self._button_add_10_random_patients.grid(row=2, column=2)
        self._button_delete_id47_patient = Button(self, text="Delete patient id=42", command=self.delete_patient_in_database_TEST, bg="#E3F6CE", fg="blue")
        self._button_delete_id47_patient.grid(row=2, column=3)

        self.pack()

    def delete_all_patients_in_database(self):
        con = sqlite.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM patient_table_good2 WHERE cnp='1' ")
        con.close()
        print ("toti pacientii cu cnp invalid au fost stersi")

    def add_10_random_patients_in_database(self):
        con = sqlite.connect('test.db')
        with con:
            cur = con.cursor()
            for i in range(10):
                firstname = 'gogu' + str(i)
                lastname = 'preda'
                cnp = '188090822435' + str(i)
                address_country = 'Romania'
                address_city = 'Iasi'
                address_street = 'Tabacului'
                occupation = 'Programmer'
                cur.execute("INSERT INTO patient_table_good3(firstname, lastname, cnp, address_country, address_city, address_street, occupation) values(?, ?, ?, ?, ?, ?, ?)",
                            (firstname, lastname, cnp, address_country, address_city, address_street, occupation))
                print ("un nou pacient *" + firstname + " " + lastname + "* a fost adaugat")
        con.close()


    def delete_patient_in_database_TEST(self):
        con = sqlite.connect('test.db')
        con.execute("PRAGMA foreign_keys = 1")
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM patient_table_good3 WHERE id = ?", (42,))
        con.close()
        print ("un delete a fost facut in Patient DB --> linia cu id = 42 a fost stearsa")


# Notebook - Tab 3
class Tab_Appointment(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self._label_1 = Label(self, text="Enter Firstname").grid(row=0)
        self._label_2 = Label(self, text="Enter Lastname").grid(row=1)
        self._label_2 = Label(self, text="Enter Appintment Day").grid(row=2)
        self._label_2 = Label(self, text="Enter Start Hour").grid(row=3)
        self._label_2 = Label(self, text="Enter Stop Hour").grid(row=4)
        self._textbox_firstname_appointment = tk.Entry(self, width=40)
        self._textbox_lastname_appointment = tk.Entry(self, width=40)
        self._textbox_day_appointment = tk.Entry(self, width=40)
        self._textbox_start_hour_appointment = tk.Entry(self, width=40)
        self._textbox_stop_hour_appointment = tk.Entry(self, width=40)
        self._textbox_firstname_appointment.grid(row=0, column=1)
        self._textbox_lastname_appointment.grid(row=1, column=1)
        self._textbox_day_appointment.grid(row=2, column=1)
        self._textbox_start_hour_appointment.grid(row=3, column=1)
        self._textbox_stop_hour_appointment.grid(row=4, column=1)
        appointment_new = Appointment("", "", "", "", "")
        self._button_add_appointment = Button(self, text="Add Appointment", command=lambda: appointment_new.add_appointment_in_database(Entry.get(self._textbox_firstname_appointment), Entry.get(self._textbox_lastname_appointment), Entry.get(self._textbox_day_appointment), Entry.get(self._textbox_start_hour_appointment), Entry.get(self._textbox_stop_hour_appointment)), bg="#E3F6CE", fg="blue")
        self._button_add_appointment.grid(row=7, column=1)
        self._button_print_appointment = Button(self, text="Print Appointment DB", command=lambda: appointment_new.print_appointment_database(), bg="#E3F6CE", fg="blue")
        self._button_print_appointment.grid(row=7, column=2)
        self.pack()


class Tab_Statistic(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self._button_add_patient = Button(self, text="See nr patients/year", command=self.show_patient_per_year_from_database, bg="#E3F6CE", fg="blue")
        self._button_add_patient.grid(row=2, column=1)
        self.pack()

    def get_year_of_birth_patient_per_country(self, cnp, country):
        year_local = 0
        if country.find('Romania') != -1:
            if ((int(cnp[1]) * 10) + int(cnp[2])) >= 30:
                year_local = 1900 + (int(cnp[1]) * 10) + int(cnp[2])
            if int(cnp[1]) == 0:
                year_local = 2000 + int(cnp[2])
            if (((int(cnp[1]) * 10) + int(cnp[2])) >= 10) & (((int(cnp[1]) * 10) + int(cnp[2])) < 30):
                year_local = 2000 + (int(cnp[1]) * 10) + int(cnp[2])
        return year_local

    def show_patient_per_year_from_database(self):
        year_local_array = []
        year_local = 0
        con = sqlite.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT cnp, address_country FROM patient_table_good3")
            rows = cur.fetchall()
            # acuma iau toate cnp-urile la rand
            for row in rows:
                cnp_local = row[0]
                country = row[1]
                print("cnp este: ", cnp_local, " si country este: ", country)
                year_local = self.get_year_of_birth_patient_per_country(cnp_local, country)
                #print (year_local)
                year_local_array.append(year_local)

        con.close()

        year_local_array.sort()
        print(year_local_array)
        dictionar_pacient_per_an = {}
        count_nr_patient_per_year = 1
        for item in year_local_array:
            nr_aparitii = year_local_array.count(item)
            dictionar_pacient_per_an[item] = [nr_aparitii]

        print(dictionar_pacient_per_an)



class Tab_Logout(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self._button_logout = Button(self, text="Log Out!", command=self.log_out_function)
        self._button_logout.pack()


    def log_out_function(self):
        old_frame = NoteBook(self)
        NoteBook.log_out_success_action(old_frame)
        widget_list = app.all_children()
        for item in widget_list:
            item.pack_forget()
        app.switch_frame(NoteBook)


#-------------------------------------------------------------------------------
#------  SignUp GUI Class  ---------------------------------------------------------
#-------------------------------------------------------------------------------
class GuiSignUpWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self._label_1 = tk.Label(self, text="Create Username for account").grid(row=0)
        self._label_2 = tk.Label(self, text="Create Password for account").grid(row=1)
        self._textbox_1 = tk.Entry(self, width=40)
        self._textbox_2 = tk.Entry(self, width=40)
        self._textbox_1.grid(row=0, column=1)
        self._textbox_2.grid(row=1, column=1)
        self._textbox_1.config(state=NORMAL)
        self._textbox_2.config(state=NORMAL)
        self._button_signup = tk.Button(self, text="Create Account", command=self.func_create_account)
        self._button_signup.grid(row=3, column=0)
        self.title="Sign Up Window"


    def func_create_account(self):
        username_local = Entry.get(self._textbox_1)
        password_local = Entry.get(self._textbox_2)
        today = date.today()
        with open("file_users_passwords.txt", 'a+') as the_file:
            the_file.write(username_local+" "+password_local+":"+str(today)+"\n")
        file.close(the_file)
        tkMessageBox.showwarning("Info", "Acoount Created with Success!")
        subprocess.check_call(["attrib", "+H", "file_users_passwords.txt"])

#-------------------------------------------------------------------------------
#------  Login GUI Class  ------------------------------------------------------
#-------------------------------------------------------------------------------
class GuiLoginWindow(tk.Tk):

    dictionar_users_and_passwords = {}
    dictionar_users_and_passwords_and_dates_of_account_creation = {}

    def __init__(self):
        tk.Tk.__init__(self)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self._label_1 = tk.Label(self, text="Enter Username").grid(row=0)
        self._label_2 = tk.Label(self, text="Enter Password").grid(row=1)
        self._textbox_1 = tk.Entry(self, width=40)
        self._textbox_2 = tk.Entry(self, width=40)
        self._textbox_1.grid(row=0, column=1)
        self._textbox_2.grid(row=1, column=1)
        self._textbox_1.config(state=NORMAL)
        self._textbox_2.config(state=NORMAL)
        self._button_login = tk.Button(self, text="Login", command=self.func_initial_login, bg="#E3F6CE",fg="blue")
        self._button_login.grid(row=2, column=1)
        self._button_signup = tk.Button(self, text="Sign Up", command=self.func_signup_login, bg="#E3F6CE")
        self._button_signup.grid(row=0, column=3)
        self.title = "Login Window"

    counter_login_tries = 0

    def func_initial_login(self):
        log = Login(Entry.get(self._textbox_1), Entry.get(self._textbox_2))
        return_database_accounts_exists = log.read_file_user_pass(self.dictionar_users_and_passwords, self.dictionar_users_and_passwords_and_dates_of_account_creation)

        if return_database_accounts_exists == 1:
            return_check = log.check(Entry.get(self._textbox_1), Entry.get(self._textbox_2), self.dictionar_users_and_passwords)
            log.check_password_too_old(Entry.get(self._textbox_1), Entry.get(self._textbox_2), self.dictionar_users_and_passwords, self.dictionar_users_and_passwords_and_dates_of_account_creation)
            if return_check == 1:
                app_login_initial.quit()
            else:
                print "Login failed!!"
                if self.counter_login_tries == 3:
                    app_login_initial._textbox_1.delete(0, END)
                    app_login_initial._textbox_2.delete(0, END)
                    app_login_initial._textbox_1.insert(1, "error")
                    app_login_initial._textbox_2.insert(1, "error")
                    app_login_initial.quit()
                    tkMessageBox.showwarning("Warning", "Login Failed!! Au trecut 3 incercari..")
                else:
                    self.counter_login_tries += 1
        else:
            tkMessageBox.showerror("Eroare", "Nu exista nici un cont in database. Sign Up first!!")


    def func_signup_login(self):
        app_signup_initial = GuiSignUpWindow()
        app_signup_initial.mainloop()



def afiseaza_database_content():

    patient_dict_from_db = {}

    con = sqlite.connect('test.db')

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM patient_table_good3')
        rows = cur.fetchall()
        print "continutul bazei de date *patient_table_good3* este --> \n"
        for row in rows:
            print row

        cur = con.cursor()
        cur.execute('SELECT * FROM appointment_table_good7')
        rows = cur.fetchall()
        print "continutul bazei de date *appointment_table_good7* este --> \n"
        for row in rows:
            print row
    con.close()


#-------------------------------------------------------------------------------
#------  Main function for whole application  ----------------------------------
#-------------------------------------------------------------------------------


if __name__ == '__main__':

    #app_login_initial = GuiLoginWindow()
    #app_login_initial.mainloop()
    app = GUI()
    app.geometry("640x480")
    app.title = "Main Application"
    app.mainloop()

    afiseaza_database_content()



