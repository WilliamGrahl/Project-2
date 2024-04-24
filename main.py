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

def starting_window():
    starter_window = tk.Tk()
    starter_window.title("Menu")
    starter_window.geometry("400x210+3650+500")

    def open_login_window():
        starter_window.destroy()
        log_in_window() 

    def open_signup_window():
        starter_window.destroy()
        sign_up_window()

    button_font = ("Helvetica", 16)

    go_to_login_button = tk.Button(starter_window, text="Sign in", command=open_login_window, font=button_font)
    go_to_login_button.pack(pady=15)

    go_to_signup_button = tk.Button(starter_window, text="Sign up", command=open_signup_window, font=button_font)
    go_to_signup_button.pack(pady=15)

    exit_button = tk.Button(starter_window, text="Exit", command=lambda: exit(), font=button_font)
    exit_button.pack(pady=15)

    starter_window.mainloop()

def log_in_window():
    global logged_in
    logged_in = False
    login_window = tk.Tk()
    login_window.title("Sign in")
    login_window.geometry("380x200+3650+500")

    label_username = tk.Label(login_window, text="Username")
    label_username.pack()
    entry_username = tk.Entry(login_window)
    entry_username.pack()

    label_password = tk.Label(login_window, text="Password")
    label_password.pack()
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack()

    error_shown = False

    def log_in():
        global logged_in
        nonlocal error_shown

        username = entry_username.get()
        password = entry_password.get()

        for account in accounts:
            if account['username'] == username and account['password'] == password:
                logged_in = True
                login_window.destroy()
                return
        
        if error_shown:
            return

        label_invalid = tk.Label(login_window, text="Incorrect username or password", fg="red")
        label_invalid.pack()
        error_shown = True 

    login_button = tk.Button(login_window, text="Sign in", command=log_in)
    login_button.pack()

    login_window.mainloop()


def sign_up_window():
    global logged_in
    logged_in = False
    signup_window = tk.Tk()
    signup_window.title("Sign up")
    signup_window.geometry("380x200+3650+500")

    label_username = tk.Label(signup_window, text="Username")
    label_username.pack()
    entry_username = tk.Entry(signup_window)
    entry_username.pack()

    label_password = tk.Label(signup_window, text="Password")
    label_password.pack()
    entry_password = tk.Entry(signup_window)
    entry_password.pack()

    error_label = tk.Label(signup_window, fg="red")
    error_label.pack()

    def sign_up():
        global logged_in
        username = entry_username.get()
        password = entry_password.get()

        found_existing = False

        for account in accounts:
            if account['username'] == username:
                error_label.config(text="Username already exists. Please choose a different one")
                found_existing = True
                break

        if not found_existing:
            accounts.append({'username': username, 'password': password})
            save_data_with_pickle(accounts, "saved_data.pkl")
            logged_in = True
            signup_window.destroy()

    signup_button = tk.Button(signup_window, text="Sign up", command=sign_up)
    signup_button.pack()

    signup_window.mainloop()
    
def analysis():
    global logged_in
    if logged_in == True: 

        main_window = tk.Tk()
        main_window.geometry("1200x600+3200+370")
        frame1 = create_omx_frame(main_window)
        frame2 = create_bitcoin_frame(main_window)
        frame3 = create_gold_frame(main_window)
        frame4 = create_USD_frame(main_window)
        frame5 = create_silver_frame(main_window)

        def show_frame_1():
            frame1.pack(fill='both', expand=1)
            frame2.pack_forget()
            frame3.pack_forget()
            frame4.pack_forget()
            frame5.pack_forget()

        def show_frame_2():
            frame2.pack(fill='both', expand=1)
            frame1.pack_forget()
            frame3.pack_forget()
            frame4.pack_forget()
            frame5.pack_forget()

        def show_frame_3():
            frame3.pack(fill='both', expand=1)
            frame1.pack_forget()
            frame2.pack_forget()
            frame4.pack_forget()
            frame5.pack_forget()

        def show_frame_4():
            frame4.pack(fill='both', expand=1)
            frame1.pack_forget()
            frame2.pack_forget()
            frame3.pack_forget()
            frame5.pack_forget()

        def show_frame_5():
            frame5.pack(fill='both', expand=1)
            frame1.pack_forget()
            frame2.pack_forget()
            frame3.pack_forget()
            frame4.pack_forget()

        def add_button(frame):
            button_font = ("Helvetica", 16)

            omx30_button = tk.Button(frame, text="Show omx30", command=show_frame_1, font=button_font)
            omx30_button.pack(side=tk.BOTTOM)

            bitcoin_button = tk.Button(frame, text="Show bitcoin", command=show_frame_2, font=button_font)
            bitcoin_button.pack(side=tk.BOTTOM)

            gold_button = tk.Button(frame, text="  Show gold  ", command=show_frame_3, font=button_font)
            gold_button.pack(side=tk.BOTTOM)

            USD_button = tk.Button(frame, text="  Show USD  ", command=show_frame_4, font=button_font)
            USD_button.pack(side=tk.BOTTOM)

            Silver_button = tk.Button(frame, text=" Show Silver ", command=show_frame_5, font=button_font)
            Silver_button.pack(side=tk.BOTTOM)

            exit_button = tk.Button(frame, text="Exit", command=lambda: exit(), font=button_font)
            exit_button.pack(pady=20)

        add_button(frame5)
        add_button(frame4)
        add_button(frame3)
        add_button(frame2)
        add_button(frame1)
            
        show_frame_1()
        main_window.mainloop()

def main():

    starting_window()

    analysis()

if __name__ == "__main__":
    main()
