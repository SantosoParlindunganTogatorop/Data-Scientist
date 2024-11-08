import pandas as pd
import os
from FileExt import add, ubah, delete, search, ubah_item
from login import login,register,data
import time


df = pd.read_csv('Data_CSV.csv')
dfa = pd.read_csv('akun.csv')


def menu(role,df):

    while True:
        os.system('cls')
        data(role)
        choice = (
            input("Pilih menu 1-7 : ")
            if role == 'admin'
            else input ("Pilih menu 1-3 : ")
        )
        if choice == '1':
            print(df)
            input("Enter untuk melanjutkan ....")
        elif choice == '2':
            add(df)
            time.sleep(3)
        elif choice == '3' and role == 'admin':
            ubah(df)
            time.sleep(3)
        elif choice == '3':
            break
        elif choice == '4' and role == 'admin':     ## -- inngat menambhakan df = kembali
            delete(df)
            time.sleep(3)
        elif choice == '5' and role == 'admin':
            search(df)
            input("Enter untuk melanjutkan ....")
        elif choice == '6' and role == 'admin':
            ubah_item(df)
            time.sleep(3)
        elif choice == '3' and role == 'admin':
            break
        else :
            print("Tidak ada pilihan !")
            time.sleep(3)


def main():
    while True:
        os.system('cls')
        print("=" * 28)
        print("==== Welcome to Program ====")
        print("=" * 28)
        print("1. Login")
        print("2. Register")
        print("3. Logout")
        print("=" * 28)
        choice = input("Pilih Salah satu untuk Masuk ke program : ")
        if choice == '1':
            role = login(dfa)
            if not role:
                print("Login Gagal")
            else:
                menu(role['role'],df)
        elif choice == '2':
            register(dfa)
        elif choice == '3':
            break
        else:
            print("Tidak ada menu pilihan !")
            time.sleep(3)
    
main()