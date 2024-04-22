from plots import *
import pickle

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


def log_in_window():
    global logged_in
    logged_in = False
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("380x170+3650+500")

    label_username = tk.Label(login_window, text="Username")
    label_username.pack()
    entry_username = tk.Entry(login_window)
    entry_username.pack()

    label_password = tk.Label(login_window, text="Password")
    label_password.pack()
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack()

    def log_in():
        global logged_in
        username = entry_username.get()
        password = entry_password.get()

        for account in accounts:
            if account['username'] == username and account['password'] == password:
                print("\nLogin successful!")
                logged_in = True
                print(f"\nWelcome {username}")
                login_window.destroy()
                return

        print("\nIncorrect username or password.")

    login_button = tk.Button(login_window, text="Login", command=log_in)
    login_button.pack()

    login_window.mainloop()


def sign_up_window():
    global logged_in
    logged_in = False
    signup_window = tk.Tk()
    signup_window.title("Sign up")
    signup_window.geometry("380x170+3650+500")

    label_username = tk.Label(signup_window, text="Username")
    label_username.pack()
    entry_username = tk.Entry(signup_window)
    entry_username.pack()

    label_password = tk.Label(signup_window, text="Password")
    label_password.pack()
    entry_password = tk.Entry(signup_window, show="*")
    entry_password.pack()

    def sign_up():
        global logged_in
        username = entry_username.get()
        password = entry_password.get()

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
            signup_window.destroy()
            return

    login_button = tk.Button(signup_window, text="Login", command=sign_up)
    login_button.pack()

    signup_window.mainloop()


def main():
    while True:
        choice = input("\nDo you want to log in, sign up or exit? ")
        if choice.lower() == "login" or choice == "log in":
            log_in_window()
            break
        elif choice.lower() == "signup" or choice == "sign up":
            sign_up_window()
            break
        elif choice.lower() == "exit":
            exit()
        else:
            print("Invalid choice. Please try again.")
            continue

    global logged_in
    if logged_in == True: 

        main_window = tk.Tk()
        main_window.geometry("1200x600+3200+370")
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