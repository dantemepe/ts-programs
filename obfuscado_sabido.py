print("finally, a fuckin app that lets me code on android!!!")

# Import system module for exit functions and time module for delays
import sys
import time
import json
import base64
import os

# Initialize default admin account credentials
rtuser = "admin"    # Root username
rtpass = "admin!."  # Root password
accname = ""        # Will store created account username
accpass = ""        # Will store created account password
Loop = False        # Control variable for account creation loop

# SIMPLE STORAGE - Use current directory only
storage_path = "./user_accounts"  # Local folder in current directory

# Create storage directory if it doesn't exist
if not os.path.exists(storage_path):
    try:
        os.makedirs(storage_path)
        print(f"Created account storage at: {storage_path}")
    except Exception as e:
        print(f"Warning: Could not create storage directory: {e}")
        storage_path = "."  # Use current directory as fallback

# ========== OBFUSCATION SYSTEM ========== #
# EXPLANATION: These functions make account data unreadable in the file
# They use character shifting + base64 encoding to hide the actual data

def obfuscate_accounts(accounts_dict):
    """
    Obfuscate accounts data using base64 + character shift
    This makes the file content look like garbage text
    """
    try:
        # STEP 1: Convert dictionary to JSON string
        # {"user1": "pass1"} becomes '{"user1": "pass1"}'
        json_str = json.dumps(accounts_dict)
        
        # STEP 2: Character shifting obfuscation
        # This scrambles the text by changing each character's ASCII value
        obfuscated = ""
        for i, char in enumerate(json_str):
            # Alternate between +1 and -1 shift for more confusion
            # Even positions: shift forward by 1, Odd positions: shift backward by 1
            shift = 1 if i % 2 == 0 else -1
            obfuscated += chr(ord(char) + shift)  # Change character code
        
        # STEP 3: Base64 encoding
        # Converts the scrambled text to base64 (looks like random letters/numbers)
        encoded = base64.b64encode(obfuscated.encode('utf-8')).decode('utf-8')
        return encoded
        
    except:
        # Fallback to simple base64 if advanced obfuscation fails
        return base64.b64encode(json.dumps(accounts_dict).encode('utf-8')).decode('utf-8')

def deobfuscate_accounts(encoded_data):
    """
    Deobfuscate accounts data - reverse the obfuscation process
    Converts the garbage text back to readable dictionary
    """
    try:
        # STEP 1: Base64 decode
        # Convert base64 string back to scrambled text
        decoded_b64 = base64.b64decode(encoded_data).decode('utf-8')
        
        # STEP 2: Reverse character shifting
        # Un-scramble the text by reversing the character shifts
        deobfuscated = ""
        for i, char in enumerate(decoded_b64):
            # Reverse the shift: Even positions: -1, Odd positions: +1
            shift = -1 if i % 2 == 0 else 1  # Opposite of obfuscation
            deobfuscated += chr(ord(char) + shift)  # Restore original character
        
        # STEP 3: Convert JSON string back to dictionary
        return json.loads(deobfuscated)
        
    except:
        try:
            # Fallback: try simple base64 decoding
            decoded = base64.b64decode(encoded_data).decode('utf-8')
            return json.loads(decoded)
        except:
            return {}  # Return empty dict if everything fails

# ========== MODIFIED ACCOUNT FUNCTIONS ========== #

def save_account_obfuscated(username, password):
    """
    Save account with obfuscation - replaces the old save function
    """
    try:
        accounts = {}
        # Changed file extension from .json to .dat for more confusion
        account_file = os.path.join(storage_path, "accounts.dat")
        
        # Load existing accounts if file exists
        if os.path.exists(account_file):
            try:
                with open(account_file, "r") as f:
                    encoded_data = f.read()  # Read the obfuscated data
                    accounts = deobfuscate_accounts(encoded_data)  # Convert back to dict
            except:
                pass  # If reading fails, start with empty accounts
        
        # Add new account to the dictionary
        accounts[username] = password
        
        # Obfuscate the entire accounts dictionary and save
        encoded_data = obfuscate_accounts(accounts)
        
        with open(account_file, "w") as f:
            f.write(encoded_data)  # Write the obfuscated data
        
        # Create user folder for file storage
        user_folder = os.path.join(storage_path, username)
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)
            create_default_files(user_folder)
        
        print(f"Account saved to secure storage!")
    except Exception as e:
        print(f"Error saving account: {e}")

def load_accounts_obfuscated():
    """
    Load accounts with deobfuscation - replaces the old load function
    """
    account_file = os.path.join(storage_path, "accounts.dat")
    
    if os.path.exists(account_file):
        try:
            with open(account_file, "r") as f:
                encoded_data = f.read()  # Read the obfuscated file
                return deobfuscate_accounts(encoded_data)  # Convert back to dict
        except Exception as e:
            print(f"Error loading accounts: {e}")
            return {}
    return {}

# ========== EXISTING FILE SYSTEM FUNCTIONS ========== #

def create_default_files(user_folder):
    try:
        # CONGRATULATIONS.txt
        with open(os.path.join(user_folder, "CONGRATULATIONS.txt"), "w") as f:
            f.write("Congrats for logging in!\nWelcome to your personal file system!")
        
        # IDK TEST.txt
        with open(os.path.join(user_folder, "IDK TEST.txt"), "w") as f:
            f.write("test :p\nThis is a test file!\nYou can edit me later!")
    except Exception as e:
        print(f"Error creating default files: {e}")

def get_user_files(username):
    user_folder = os.path.join(storage_path, username)
    files = []
    
    if os.path.exists(user_folder):
        try:
            for file in os.listdir(user_folder):
                if file.endswith('.txt'):
                    files.append(file)
        except:
            pass
    
    return files

def read_file(username, filename):
    try:
        file_path = os.path.join(storage_path, username, filename)
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                return f.read()
        return "File not found!"
    except:
        return "Error reading file!"

def write_file(username, filename, content):
    try:
        file_path = os.path.join(storage_path, username, filename)
        with open(file_path, "w") as f:
            f.write(content)
        return True
    except:
        return False

def create_new_file(username, filename, content):
    try:
        # Ensure .txt extension
        if not filename.endswith('.txt'):
            filename += '.txt'
        
        file_path = os.path.join(storage_path, username, filename)
        with open(file_path, "w") as f:
            f.write(content)
        
        return filename
    except:
        return None

def display_files_menu(files):
    print("                                                 0. [ACCOUNT_DATA].ini")
    print(" ")
    print("                                               ")
    
    # Display existing files
    for i, file in enumerate(files, 1):
        print(f" {i}.              [{file}]      ")
        time.sleep(0.2)
    
    # ALWAYS show "Create .txt file" as the last option
    create_option_num = len(files) + 1
    print(f" {create_option_num}.              [Create .txt file].exe     ")
    time.sleep(0.2)
    
    print(" ")
    time.sleep(1)

# ========== MAIN PROGRAM LOGIC ========== #

# Load accounts using OBFUSCATED system instead of simple system
all_accounts = load_accounts_obfuscated()

print("")

# Ask user if they want to create account or login
print("Create account or log in?")
AOL = input(" (1)Create account      (2)Log in     >  ")

if AOL == "1":
    while not Loop:
        accname = input(" Insert account name  > ")
        accpass = input(" Insert account password  > ")
        accrecheck = input(" Please retype your password for confirmation  > ")
        
        if accrecheck == accpass:
            print(" ")
            print("Account created successfully!")
            # Save using OBFUSCATED system instead of simple system
            save_account_obfuscated(accname, accpass)
            # Reload accounts to include new one
            all_accounts = load_accounts_obfuscated()
            Loop = True
        else:
            print(" ")
            print("Passwords are not the same, please retry.")
elif AOL == "2":
    pass
else:
    print("Invalid option! Closing program...")
    time.sleep(1)
    sys.exit(1)

print(" ")
time.sleep(0.5)
print("Please Log in:")
user = input(" enter username  > ")
time.sleep(0.3)
passw = input(" enter password  > ")
time.sleep(0.2)

if (user == rtuser and passw == rtpass) or (user in all_accounts and all_accounts[user] == passw):
    print("Successfully logged in!") 
    
    user_files = get_user_files(user)
    
    if not user_files and user != rtuser:
        user_folder = os.path.join(storage_path, user)
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)
        create_default_files(user_folder)
        user_files = get_user_files(user)
    
    display_files_menu(user_files)
    
    file_choice = input(" Insert Number of file to access  > ")
    
    if file_choice == "0":
        print("Accessing account info...")
        time.sleep(0.5)
        pcheck = input("Ingress password to access information  : ")
        if (user == rtuser and pcheck == rtpass) or (user in all_accounts and pcheck == all_accounts[user]):
            print("Valid password, Displaying data on screen")
            time.sleep(0.3)
            print("")
            print("Account Username:", user)
            print("Account Password: *****")
            print("To show password type 'Y'")
            print(" ")
            passcheck = input("Show password (Y/N)  > ")
            if passcheck.lower() == "y":
                print("")
                print("Account Username:", user)
                if user == rtuser:
                    print("Account Password:", rtpass)
                else:
                    print("Account Password:", all_accounts[user])
                print("")
                time.sleep(3)
            input("Press Enter to close program...")
            sys.exit(0)
        else:
            print("Invalid password! Closing program...")
            time.sleep(1)
            sys.exit(3)
    
    elif file_choice.isdigit() and 1 <= int(file_choice) <= len(user_files):
        file_index = int(file_choice) - 1
        selected_file = user_files[file_index]
        
        print(" ")
        print(f"=== Content of {selected_file} ===")
        content = read_file(user, selected_file)
        print(content)
        print("=" * (len(selected_file) + 20))
        
        edit_choice = input("Do you want to edit this file? (Y/N)  > ")
        if edit_choice.lower() == "y":
            print("Enter new content (press Enter twice to finish):")
            new_content = ""
            while True:
                line = input()
                if line == "":
                    break
                new_content += line + "\n"
            
            if write_file(user, selected_file, new_content.strip()):
                print("File updated successfully!")
            else:
                print("Error updating file!")
        
        input("Press Enter to close program...")
        sys.exit(0)
    
    elif file_choice.isdigit() and int(file_choice) == len(user_files) + 1:
        new_filename = input("Enter name for new file (without .txt)  > ")
        print("Enter content for new file (press Enter twice to finish):")
        new_content = ""
        while True:
            line = input()
            if line == "":
                break
            new_content += line + "\n"
        
        created_file = create_new_file(user, new_filename, new_content.strip())
        if created_file:
            print(f"File '{created_file}' created successfully!")
            
            print("\nUpdated file list:")
            user_files = get_user_files(user)
            display_files_menu(user_files)
            
            view_new = input("Would you like to view your new file? (Y/N)  > ")
            if view_new.lower() == "y":
                print(" ")
                print(f"=== Content of {created_file} ===")
                content = read_file(user, created_file)
                print(content)
                print("=" * (len(created_file) + 20))
        else:
            print("Error creating file!")
        
        input("Press Enter to close program...")
        sys.exit(0)
    
    else:
        print("Invalid file selection! Closing program...")
        time.sleep(1)
        sys.exit(2)

else:
    print("incorrect username or password!")
    time.sleep(0.85)
    sys.exit(4)