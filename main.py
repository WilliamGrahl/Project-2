import pickle
from plots import open_tkinter_window_1
from plots import open_tkinter_window_2
from plots import open_tkinter_window_3

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
            print("1. Stay")
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
            print("1. Stay")
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
        while True:
            print("\n1. OMX30")
            print("2. BITCOIN")
            print("3. GOLD")
            myAnswer = input("\nWhich one do you want to look at? Type in the number: ")
            if myAnswer == "1":
                open_tkinter_window_1()
                break
            elif myAnswer == "2":
                open_tkinter_window_2()
                break
            elif myAnswer == "3":
                open_tkinter_window_3()
                break
            else:
                print("Wrong input, try again.")
                continue

if __name__ == "__main__":
    main()