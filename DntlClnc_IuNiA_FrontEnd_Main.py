from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from datetime import date
import datetime
import os.path
import subprocess

import DntlClnc_IuNiA_Patient as patient_file
from DntlClnc_IuNiA_Login import Login
from DntlClnc_IuNiA_Patient import Patient
from DntlClnc_IuNiA_Appointment import Appointment
from DntlClnc_IuNiA_Treatment import Treatment
from DntlClnc_IuNiA_Treatment import TreatmentPlan
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
        self._tab4 = Tab_Treatment(self._notebook)
        self._tab5 = Tab_Statistic(self._notebook)
        self._tab6 = Tab_Logout(self._notebook)
        self._notebook.add(self._tab0, text="Login")
        self._notebook.add(self._tab1, text="Main Window")
        self._notebook.add(self._tab2, text="Patient Win")
        self._notebook.add(self._tab3, text="Appointment Win")
        self._notebook.add(self._tab4, text="Treatment Win")
        self._notebook.add(self._tab5, text="Statistics")
        self._notebook.add(self._tab6, text="Logout")
        self._notebook.tab(1, state="disabled")
        self._notebook.tab(2, state="disabled")
        self._notebook.tab(3, state="disabled")
        self._notebook.tab(4, state="disabled")
        self._notebook.tab(5, state="disabled")
        self._notebook.tab(6, state="disabled")
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
        self._tab4 = Tab_Treatment(self._notebook)
        self._tab5 = Tab_Statistic(self._notebook)
        self._tab6 = Tab_Logout(self._notebook)
        self._notebook.add(self._tab0, text="Login")
        self._notebook.add(self._tab1, text="Main Window")
        self._notebook.add(self._tab2, text="Patient Win")
        self._notebook.add(self._tab3, text="Appointment Win")
        self._notebook.add(self._tab4, text="Treatment Win")
        self._notebook.add(self._tab5, text="Statistics")
        self._notebook.add(self._tab6, text="Logout")
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
        self._textbox_1.insert(0, "asd")
        self._textbox_2.insert(0, "dasd")
        self._button_login = tk.Button(self, text="Login", command=self.func_initial_login, bg="#E3F6CE", fg="blue")
        self._button_login.grid(row=2, column=1)
        self._button_signup = tk.Button(self, text="Sign Up", command=self.func_signup_login, bg="#E3F6CE")
        self._button_signup.grid(row=0, column=3, sticky=W, pady=2)
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
                print("Login failed!!")
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

    iiii = 0

    def __init__(self, master):
        Frame.__init__(self, master)
        self.labelFrame = LabelFrame(self, text = "Add New Patient")
        self.labelFrame.grid(padx = 10, pady = 10)
        self._label_1 = Label(self.labelFrame, text="Enter Firstname").grid(row=0)
        self._label_2 = Label(self.labelFrame, text="Enter Lastname").grid(row=1)
        self._label_2 = Label(self.labelFrame, text="Enter CNP").grid(row=2)
        self._label_2 = Label(self.labelFrame, text="Enter Country").grid(row=3)
        self._label_2 = Label(self.labelFrame, text="Enter City").grid(row=4)
        self._label_2 = Label(self.labelFrame, text="Enter Street").grid(row=5)
        self._label_2 = Label(self.labelFrame, text="Enter Occupation").grid(row=6)
        self._textbox_firstname_patient = tk.Entry(self.labelFrame, width=40)
        self._textbox_lastname_patient = tk.Entry(self.labelFrame, width=40)
        self._textbox_cnp_patient = tk.Entry(self.labelFrame, width=40)
        self._textbox_country_patient = tk.Entry(self.labelFrame, width=40)
        self._textbox_city_patient = tk.Entry(self.labelFrame, width=40)
        self._textbox_street_patient = tk.Entry(self.labelFrame, width=40)
        self._textbox_occupation_patient = tk.Entry(self.labelFrame, width=40)
        self._textbox_firstname_patient.grid(row=0, column=1)
        self._textbox_lastname_patient.grid(row=1, column=1)
        self._textbox_cnp_patient.grid(row=2, column=1)
        self._textbox_country_patient.grid(row=3, column=1)
        self._textbox_city_patient.grid(row=4, column=1)
        self._textbox_street_patient.grid(row=5, column=1)
        self._textbox_occupation_patient.grid(row=6, column=1)
        patient_new = Patient("", "", "", "", "", "", "")
        self._button_add_patient = Button(self.labelFrame, text="Add patient", command=lambda: patient_new.add_patient_in_database(Entry.get(self._textbox_firstname_patient), Entry.get(self._textbox_lastname_patient), Entry.get(self._textbox_cnp_patient), Entry.get(self._textbox_country_patient), Entry.get(self._textbox_city_patient), Entry.get(self._textbox_street_patient), Entry.get(self._textbox_occupation_patient)), bg="#E3F6CE", fg="blue")
        self._button_add_patient.grid(row=5, column=2)
        self._button_delete_all_patients = Button(self.labelFrame, text="Delete All Patients", command=self.delete_all_patients_in_database, bg="#E3F6CE", fg="blue")
        self._button_delete_all_patients.grid(row=1, column=2)
        self._button_add_10_random_patients = Button(self.labelFrame, text="Add 10 Random Patients", command=self.add_10_random_patients_in_database, bg="#E3F6CE", fg="blue")
        self._button_add_10_random_patients.grid(row=2, column=2)
        self._button_delete_id47_patient = Button(self.labelFrame, text="Delete patient id=42", command=self.delete_patient_in_database_TEST, bg="#E3F6CE", fg="blue")
        self._button_delete_id47_patient.grid(row=3, column=2)
        self._button_show_all_patients = Button(self.labelFrame, text="Show all patients", command=afiseaza_database_content, bg="#E3F6CE", fg="blue")
        self._button_show_all_patients.grid(row=4, column=2)

        #bt = ttk.Button(self, text='Add Row', command=self.add_row)
        #bt.grid(row=8, column=0)

        #dl = ttk.Button(self, text='Delete Row')
        #dl.grid(row=8, column=1)

        #v0 = StringVar()
        #e0 = Entry(self, textvariable=v0, state='readonly')
        #v0.set('Select')
        #e0.grid(row=9, column=0)

        #v1 = StringVar()
        #e1 = Entry(self, textvariable=v1, state='readonly')
        #v1.set('Col1')
        #e1.grid(row=9, column=1)

        #v2 = StringVar()
        #e2 = Entry(self, textvariable=v2, state='readonly')
        #v2.set('Col2')
        #e2.grid(row=9, column=2)

        #v3 = StringVar()
        #e3 = Entry(self, textvariable=v3, state='readonly')
        #v3.set('Col3')
        #e3.grid(row=9, column=3)

        #v4 = StringVar()
        #e4 = Entry(self, textvariable=v4, state='readonly')
        #v4.set('Col4')
        #e4.grid(row=9, column=4)

        sizex = 800
        sizey = 600
        posx = 100
        posy = 100
        #self.winfom_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

        self.labelFrame_SearchPatient = LabelFrame(self, text="Search Patient")
        self.labelFrame_SearchPatient.grid(padx=50, pady=10)

        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback_search_when_typing(sv))
        self._textbox_search_patient = tk.Entry(self.labelFrame_SearchPatient, textvariable=sv)
        self._textbox_search_patient.grid(row=0, column=0)
        self._button_edit_patient = Button(self.labelFrame_SearchPatient, command=self.edit_patient_in_database, text="Edit patient info", bg="#E3F6CE", fg="blue")
        self._button_edit_patient.grid(row=1, column=1)
        #self._button_edit_patient.bind("<Button-1>", self.edit_patient_in_database)
        self._ListBox_SearchPatient = tk.Listbox(self.labelFrame_SearchPatient, width=30, height=10)
        self._ListBox_SearchPatient.grid(row=1, column=0)
        #self._ListBox_SearchPatient.bind('<<ListboxSelect>>', self.callback_when_click_on_found_item)
        self._ListBox_SearchPatient.bind('<Double-1>', self.callback_when_doubleclick_on_found_item)


    def callback_search_when_typing(self, sv):
        self._ListBox_SearchPatient.delete(0, END)
        len_max = 0
        input = sv.get()
        patient_local_list = Patient.search_patient_in_database(Patient, input)
        for m in patient_local_list:
            if len(m) > len_max:
                len_max = len(m)

        if not patient_local_list:
            pass
            #self._ListBox_SearchPatient.delete(0,END)
        else:
            for item in patient_local_list:
                #item.configure(font=("Times New Roman", 12, "bold"))
                #f = tk.font(font=item.cget(input))
                #f.configure(underline=True, weight='bold', slant='italic')
                #self.highlight_text('tag1', 1, 1, 5,'red')
                self.add_row(item, len_max)
                #self._ListBox_SearchPatient.itemconfig(0, {'bg': 'red'})
                bolded = font.Font(weight='bold')  # will use the default font
                self._ListBox_SearchPatient.config(font=bolded)


    #def highlight_text(self, tag_name, lineno, start_char, end_char, bg_color=None, fg_color=None):
    #    self._ListBox_SearchPatient.tag_add(tag_name, f'{lineno}.{start_char}', f'{lineno}.{end_char}')
    #    self._ListBox_SearchPatient.tag_config(tag_name, background=bg_color, foreground=fg_color)


    def callback_when_click_on_found_item(self, event):
        cursor_position = self._ListBox_SearchPatient.curselection()
        text_item_ListBox = self._ListBox_SearchPatient.get(cursor_position[0],END)
        #print(text_item_ListBox)
        messagebox.showinfo("Title", "Ai dat click pe Listbox item -> "+ str(text_item_ListBox[0]))

    def callback_when_doubleclick_on_found_item(self,event):
        cursor_position = self._ListBox_SearchPatient.curselection()
        text_item_ListBox = self._ListBox_SearchPatient.get(cursor_position[0], END)
        string_text_selectat = text_item_ListBox[0]
        list_string_text_selectat = string_text_selectat.split(" ")
        con = sqlite.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT * from patient_table_good3 WHERE firstname LIKE ? AND lastname LIKE ?", (list_string_text_selectat[0], list_string_text_selectat[1]))
            rows = cur.fetchall()

        con.close()

        age = (rows[0])[0]
        lastname = (rows[0])[1]
        firstname = (rows[0])[2]
        cnp = (rows[0])[3]
        adress = str((rows[0])[6]) + ", "+ str((rows[0])[5]) + ", "+str((rows[0])[4])
        occupation = (rows[0])[7]
        messagebox.showinfo("Patient Info -->" + str(string_text_selectat), "Name: " + str(lastname) + " " +str(firstname) + "\n" +"Age: " + str(age) + "\n" +"CNP: " + str(cnp) + "\n" +"Adress: " + adress + "\n" + "Occupation: " + str(occupation) + "\n")


    def edit_patient_in_database(self):
        cursor_position = self._ListBox_SearchPatient.curselection()
        text_item_ListBox = self._ListBox_SearchPatient.get(cursor_position[0], END)
        string_text_selectat = text_item_ListBox[0]

        list_string_text_selectat = string_text_selectat.split(" ")
        patient_local_list = []
        con = sqlite.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT * from patient_table_good3 WHERE firstname LIKE ? AND lastname LIKE ?", (list_string_text_selectat[0], list_string_text_selectat[1]))
            rows = cur.fetchall()
        con.close()

        #window = tk.Toplevel(self)
        window1 = tk.Toplevel()
        window1.geometry("300x300+500+200")
        window1["bg"] = "navy"
        lb = tk.Label(window1, text="Hello")
        lb.pack()
        #window.title("Edit Patient Info -->" + string_text_selectat)
        #window.("Edit Patient Info -->" + string_text_selectat)
        #w = tk.Label(window, text="Edit Patient Info -->" + string_text_selectat)
        #window.geometry("300x150+30+30")
        #topButton = window.Button(window, text="CLOSE", command=window.destroy)
        #topButton.pack()
        #window.textbox_1 = tk.Entry(window, width=30).pack(side=tk.LEFT)
        #window.textbox_2 = tk.Entry(window, width=30)
        #window.textbox_1.grid(row=2, col=0)
        #window.textbox_3 = tk.Entry(window, width=30)
        #window.textbox_1.grid(row=3, col=0)
        #window.textbox_4 = tk.Entry(window, width=30)
        #window.textbox_1.grid(row=4, col=0)
        #window.textbox_5 = tk.Entry(window, width=30)
        #window.textbox_1.grid(row=5, col=0)


    def myfunction(event,canvas):
            canvas.configure(scrollregion=canvas.bbox("all"), width=200, height=200)


    def add_row(self, text_from_list, len_max):
        self._ListBox_SearchPatient.insert("end", text_from_list)


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
            cur.execute("DELETE FROM patient_table_good3 WHERE id = ?", (81,))
        con.close()
        print ("un delete a fost facut in Patient DB --> linia cu id = 81 a fost stearsa")


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


class Tab_Treatment(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self._label_1 = Label(self, text="Enter New Treatment Name").grid(row=0)
        self._textbox_treatment_name = tk.Entry(self, width=40)
        self._textbox_treatment_name.grid(row=0, column=1)
        self._label_1 = Label(self, text="Enter New Treatment Cost").grid(row=1)
        self._textbox_treatment_cost = tk.Entry(self, width=40)
        self._textbox_treatment_cost.grid(row=1, column=1)
        treatment_new = Treatment("","")
        self._button_add_treatment = Button(self, text="Add Treatment", command=lambda: treatment_new.add_treatment_in_database(Entry.get(self._textbox_treatment_name),Entry.get(self._textbox_treatment_cost)), bg="#E3F6CE", fg="blue")
        self._button_add_treatment.grid(row=0, column=2)
        self._button_show_treatments = Button(self, text="Show Treatments from DB", command=lambda: treatment_new.print_treatment_database(), bg="#E3F6CE", fg="blue")
        self._button_show_treatments.grid(row=1, column=2)
        treatmentPlan_new = TreatmentPlan("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        self._label_1 = Label(self, text="Patient Name for TreatmentPlan").grid(row=2)
        self._textbox_patient_name_for_treatment_plan = tk.Entry(self, width=40)
        self._textbox_patient_name_for_treatment_plan.grid(row=2, column=1)
        self._label_1 = Label(self, text="Treatment Name for TreatmentPlan").grid(row=3)
        self._textbox_patient_name_for_treatment_plan.insert(0,"Negru Ovidiu")
        self._textbox_treatment_name_for_treatment_plan = tk.Entry(self, width=40)
        self._textbox_treatment_name_for_treatment_plan.grid(row=3, column=1)
        self._textbox_treatment_name_for_treatment_plan.insert(0,"implant")
        self._textbox_treatment_name_for_treatment_plan1 = tk.Entry(self, width=40)
        self._textbox_treatment_name_for_treatment_plan1.grid(row=4, column=1)
        self._textbox_treatment_name_for_treatment_plan1.insert(0,"extractie")
        self._button_add_treatmentsPlan = Button(self, text="Add TreatmentPlan", command=lambda: treatmentPlan_new.add_treatmentPlan_in_database(Entry.get(self._textbox_patient_name_for_treatment_plan), str("TreatmentPlan" + Entry.get(self._textbox_patient_name_for_treatment_plan)), Entry.get(self._textbox_treatment_name_for_treatment_plan), 1, "-", 0, "-", 0, "-", 0, "-", 0, "-", 0, "-", 0, "-", 0, "-", 0, "-", 0, 0, 0), bg="#E3F6CE", fg="blue")
        self._button_add_treatmentsPlan.grid(row=4, column=2)
        self._button_print_treatmentsPlan = Button(self, text="Print all TreatmentPlans", command=lambda: treatmentPlan_new.print_treatmentPlan_database())
        self._button_print_treatmentsPlan.grid(row=5, column=2)
        self.pack()


class Tab_Statistic(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self._button_add_patient = Button(self, text="See nr patients/year", command=self.show_patient_per_year_from_database, bg="#E3F6CE", fg="blue")
        self._button_add_patient.grid(row=2, column=1)
        self._button_patients_ages_descending_order = Button(self, text="Descending age patients", command=self.show_patient_ages_descending_order_from_database, bg="#E3F6CE", fg="blue")
        self._button_patients_ages_descending_order.grid(row=2, column=2)
        self.pack()

    def show_patient_ages_descending_order_from_database(self):
        lista_all_tuples_age_name_patient = []
        con = sqlite.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT cnp, address_country, firstname, lastname FROM patient_table_good3")
            rows = cur.fetchall()
            for row in rows:
                cnp_local = row[0]
                country = row[1]
                firstname = row[2]
                lastname = row[3]
                year_local = self.get_year_of_birth_patient_per_country(cnp_local, country)
                now = datetime.datetime.now()
                age_year_local = int(now.year) - year_local
                nume = firstname + lastname
                tuplu_age_name = (age_year_local, nume)
                lista_all_tuples_age_name_patient.append(tuplu_age_name)
        con.close()

        lista_all_tuples_age_name_patient.sort(reverse=TRUE, key=lambda tup: tup[0])
        for item in lista_all_tuples_age_name_patient:
            print(item)


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
                print("Login failed!!")
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
            messagebox.showerror("Eroare", "Nu exista nici un cont in database. Sign Up first!!")


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
        print("continutul bazei de date *patient_table_good3* este --> \n")
        for row in rows:
            print(row)

        cur = con.cursor()
        cur.execute('SELECT * FROM appointment_table_good7')
        rows = cur.fetchall()
        print("continutul bazei de date *appointment_table_good7* este --> \n")
        for row in rows:
            print(row)
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



