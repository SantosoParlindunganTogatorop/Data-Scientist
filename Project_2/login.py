import time
import os

def login(df):                                  # login 3 kali kesempatan
    i = 0
    while i<3:
        os.system('cls')
        name = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()
        
        for index, row in df.iterrows():
            if row['username'] == name and row['password'] == password:
                os.system('cls')
                print("Login Succesful")
                time.sleep(2)
                return {'username': row['username'], 'role': row['role']}
            
        os.system('cls')    
        print("Username and Pasaword not found, please register first !")
        i+=1
        time.sleep(2)
        return None
    


def register(df):
    try:
        name = input("Masukkan username : ")
        password = input("Masukkan password : ")
        if not name or not password :
            raise Exception ("Username and Password can't be empty, please try again !")
        else :
            df.loc[len(df)] = [name,password,'user'] 
            df.to_csv('akun.csv', index = False)
            os.system('cls')
            print("Register Succesful")
            time.sleep(2)
    except Exception as e:
        os.system('cls')
        print(e)
        time.sleep(2)
    except:
        print("Register Error !")
    return df


def data(role):
    os.system('cls')
    print("="*28)
    print("======= Menu Program =======")
    print("="*28)
    print("1. Read Data")
    print("2. Create Data")
    if role == 'admin':
        print("3. Change Data")
        print("4. Delete Data")
        print("5. Search Data")
        print("6. Change one of the Data")
        print("7. Logout")
        print("="*28)
    else:
        print("3. Logout")
        print("="*28)
    return role

