import Tkinter
from Tkinter import *
import Tkinter as tk
import tkMessageBox
from datetime import date
import os.path
import subprocess



class Login:

    def __init__(self, id, pas):
        self.id = id
        self.pas = pas

    def read_file_user_pass(self, dictionar_1, dictionar_2):
        cnt = 1
        if os.path.isfile("file_users_passwords.txt"):
            filepath = "file_users_passwords.txt"
            with open(filepath) as fp:
                line = fp.readline()
                while line:
                    print("Line {}: {}".format(cnt, line.strip()))
                    user, password = line.split(" ")
                    password, data_crearii_contului = password.split(":")
                    dictionar_1[user] = password
                    data_crearii_contului, nu_conteaza = data_crearii_contului.split("\n")
                    dictionar_2[user+"_"+password] = data_crearii_contului
                    line = fp.readline()
                    cnt += 1

            for x, y in dictionar_1.items():
                print(x, y)

            return_file_exists = 1
        else:
            return_file_exists = 0
        return return_file_exists

    def check(self, id, pas, dictionar_1):
        return_var = 0
        for x, y in dictionar_1.items():
            if self.id == x and self.pas == y:
                print "Login success!"
                return_var = 1
                break
            else:
                return_var = 0
        return return_var

    def check_password_too_old(self, id, pas, dictionar_1, dictionar_2):
        for x, y in dictionar_1.items():
            if self.id == x and self.pas == y:
                print "Login sfarsit cu success! Acum verificam daca parola e prea veche si trebuie schimbata..."
                username_plus_parola = x+"_"+y
                for xx, yy in dictionar_2.items():
                    if username_plus_parola == xx:
                        data_cont = yy
                        if data_cont != str(date.today()):
                            tkMessageBox.showwarning("Warning","parola cam veche, tre sa o schimbi!!!")
                            break
                        else:
                            tkMessageBox.showinfo("Info","parola ok, am verificat doar valabilitatea ;) ")
                            break




