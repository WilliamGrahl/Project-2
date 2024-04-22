import tkinter as tk
import pickle
from plots import *

def save_data_with_pickle(data, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
    except Exception as e:
        print("An error occurred:", e)

def load_data_with_pickle(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data
    except EOFError as e:
        return None
    except Exception as e:
        print("An error occurred", e)
        exit()

accounts = load_data_with_pickle("saved_data.pkl")
if accounts is None:
    accounts = []


def log_in():
    while True:
        global logged_in
        global username
        logged_in = False
        username = input("\nEnter your username: ")
        password = input("Enter your password: ")
        
        for account in accounts:
            if account['username'] == username and account['password'] == password:
                print("\nLogin successful!")
                print(f"\nWelcome {username}")
                logged_in = True
                return
            
        while True:
            print("\nIncorrect username or password.")
            print("Do you want to:")
            print("1. Try")
            print("2. Go to starting menu")
            print("3. Exit")
            try:
                choice = int(input())    
                if choice == 1:
                    break  
                elif choice == 2:
                    main()
                    return
                elif choice == 3:
                    exit()
                else:
                    print("Invalid input. Please try again")
            except ValueError:
                print("Invalid input. Please enter a number.")
        

def sign_up():
    while True:
        global logged_in
        logged_in = False
        username = input("\nEnter a username: ")
        password = input("Enter a password: ")
        
        foundExisting = False

        for account in accounts:
            if account['username'] == username:
                print("\nUsername already exists. Please choose a different one.")
                foundExisting = True
                
        if foundExisting == False:
            accounts.append({'username': username, 'password': password})
            save_data_with_pickle(accounts, "saved_data.pkl")
            print("\nAccount created successfully.\n")
            print(f"Welcome {username}")
            logged_in = True
            return

        while True:
            print("Do you want to:")
            print("1. Try again")
            print("2. Go to starting menu")
            print("3. Exit")
            try:
                choice = int(input())    
                if choice == 1:
                    break  
                elif choice == 2:
                    main()
                    return
                elif choice == 3:
                    exit()
                else:
                    print("Invalid input. Please try again")
            except ValueError:
                print("Invalid input. Please enter a number.")   

def main():
    while True:
        choice = input("\nDo you want to log in, sign up or exit? ")
        if choice.lower() == "login" or choice == "log in":
            log_in()
            break
        elif choice.lower() == "signup" or choice == "sign up":
            sign_up()
            break
        elif choice.lower() == "exit":
            exit()
        else:
            print("Invalid choice. Please try again.")
            continue

    global logged_in
    if logged_in == True: 

        main_window = tk.Tk()
        main_window.geometry("1200x600")
        frame1 = create_omx_frame(main_window)
        frame2 = create_bitcoin_frame(main_window)
        frame3 = create_gold_frame(main_window)

        def show_frame_1():
            frame1.pack(fill='both', expand=1)
            frame2.pack_forget()
            frame3.pack_forget()

        def show_frame_2():
            frame2.pack(fill='both', expand=1)
            frame1.pack_forget()
            frame3.pack_forget()

        def show_frame_3():
            frame3.pack(fill='both', expand=1)
            frame1.pack_forget()
            frame2.pack_forget()

        def add_button(frame):
            omx30_button = tk.Button(frame, text="Show omx30", command=show_frame_1)
            omx30_button.pack(side=tk.BOTTOM)

            bitcoin_button = tk.Button(frame, text="Show bitcoin", command=show_frame_2)
            bitcoin_button.pack(side=tk.BOTTOM)

            gold_button = tk.Button(frame, text="Show gold", command=show_frame_3)
            gold_button.pack(side=tk.BOTTOM)

        add_button(frame3)
        add_button(frame2)
        add_button(frame1)
            
        show_frame_1()
        main_window.mainloop()

if __name__ == "__main__":
    main()