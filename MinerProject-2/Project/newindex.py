import csv
import bcrypt
import re
import requests
import certifi
import time
from prettytable import PrettyTable  # For user-friendly tables

MAX_ATTEMPTS = 5
attempts = 0
BASE_URL = "https://www.cheapshark.com/api/1.0"

# Password hashing functions
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_password.encode())

# Input validation functions
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_password(password):
    if (len(password) >= 8 and 
        re.search(r"[A-Z]", password) and 
        re.search(r"[a-z]", password) and 
        re.search(r"\d", password) and 
        re.search(r"[!@#$%^&*]", password)):
        return True
    return False

# Save user data to CSV
def save_user_data_to_csv(email, hashed_password, security_question, hashed_answer):
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, hashed_password, security_question, hashed_answer])
    print("✅ User data saved to users.csv")

# User registration
def register_user():
    print("\n---- User Registration ----")
    email = input("Enter your email: ")
    if not is_valid_email(email):
        print("❌ Invalid email format.")
        return
    
    password = input("Enter a password: ")
    if not is_valid_password(password):
        print("❌ Password must be at least 8 characters, with upper and lower case letters, numbers, and special characters.")
        return

    security_question = "What is your favorite color?"
    security_answer = input(f"Answer the security question - {security_question}: ")
    
    hashed_password = hash_password(password)
    hashed_answer = hash_password(security_answer)

    save_user_data_to_csv(email, hashed_password, security_question, hashed_answer)

    print("✅ Registration successful.")

# Login function
def login():
    print("\n---- User Login ----")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                if check_password(row[1], password):
                    print("✅ Login successful.")
                    return True
                else:
                    print("❌ Incorrect password.")
                    return False
    print("❌ User not found.")
    return False

# Forgot password process
def forgot_password():
    print("\n---- Forgot Password ----")
    email = input("Enter your registered email: ")

    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        users = list(reader)

    for user in users:
        if user[0] == email:
            print(f"Security Question: {user[2]}")
            answer = input("Answer: ")

            if check_password(user[3], answer):
                new_password = input("Enter a new password: ")
                if is_valid_password(new_password):
                    user[1] = hash_password(new_password)
                    with open('users.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(users)
                    print("✅ Password reset successful.")
                else:
                    print("❌ New password does not meet the criteria.")
            else:
                print("❌ Incorrect answer.")
            return
    print("❌ Email not found.")

# Login with attempt limitation
def login_with_attempts():
    global attempts
    while attempts < MAX_ATTEMPTS:
        if login():
            return True
        attempts += 1
        print(f"⚠️ Attempts left: {MAX_ATTEMPTS - attempts}")
    print("❌ Maximum attempts reached. Exiting.")
    exit()

# Fetch deals from CheapShark API
def get_deals(store_id=1, upper_price=15):
    session = requests.Session()
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    params = {
        "storeID": store_id,   # Default Steam (storeID = 1)
        "upperPrice": upper_price,
        "sortBy": "Deal Rating"
    }
    
    try:
        response = session.get(f"{BASE_URL}/deals", params=params, headers=headers, verify=certifi.where())
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
        return None

# Save fetched deals to CSV
def save_deals_to_csv(deals):
    filename = 'game_deals.csv'
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Normal Price", "Sale Price", "Savings", "Deal Rating", "Deal Link"])
        
        for deal in deals:
            deal_link = deal.get('dealLink', f"https://www.cheapshark.com/redirect?dealID={deal.get('dealID', 'N/A')}")
            writer.writerow([deal['title'], deal['normalPrice'], deal['salePrice'], deal['savings'], deal['dealRating'], deal_link])
    
    print(f"✅ Game deals saved to {filename}")

# Display deals in console with specific format
def display_deals(deals):
    if not deals:
        print("❌ No deals found.")
        return

    print("\n💥 TOP GAME DEALS 💥")
    for deal in deals[:5]:  # Display top 5 deals
        deal_link = deal.get('dealLink', f"https://www.cheapshark.com/redirect?dealID={deal.get('dealID', 'N/A')}")
        print("------------------------------------------------")
        print(f"🎮 Game Title: {deal['title']}")
        print(f"🛒 Store Name: {deal.get('store', 'Unknown Store')}")
        print(f"💲 Normal Price: ${deal['normalPrice']}")
        print(f"💲 Sale Price: ${deal['salePrice']}")
        print(f"💰 Savings: {deal['savings']}%")
        print(f"⭐ Deal Rating: {deal['dealRating']}")
        print(f"🔗 Link to Store: {deal_link}")
        print("------------------------------------------------")

# Search game by title from CheapShark API
def search_game_by_title(game_title):
    session = requests.Session()
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    params = {
        "title": game_title,
        "sortBy": "Deal Rating"
    }
    
    try:
        response = session.get(f"{BASE_URL}/games", params=params, headers=headers, verify=certifi.where())
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
        return None

# Main API call and user interaction
def mainApicall():
    while True:
        print("\n🎮 What would you like to do?")
        print("1️⃣ Search for game price")
        print("2️⃣ Display the top game deals")
        print("3️⃣ Save deals to file")
        print("4️⃣ Logout")
        choice = input("Enter your response: ")

        if choice == '1':
            game_title = input("Enter the game title to search for: ")
            deals = search_game_by_title(game_title)
            if deals:
                display_deals(deals)
            else:
                print(f"❌ No deals found for {game_title}.")
        
        elif choice == '2':
            deals = get_deals()
            if deals:
                display_deals(deals)
            else:
                print("❌ No deals to display.")
        
        elif choice == '3':
            deals = get_deals()
            if deals:
                save_deals_to_csv(deals)
            else:
                print("❌ No deals to save.")
        
        elif choice == '4':
            print("🔒 Logging out.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Main function to handle user choices
if __name__ == "__main__":
    print("<---------------------------------------------->")
    print("<---------------------------------------------->")
    print("|| 🎮 Welcome to the Game Price Checker by Harsh Jaiswal 🎮 ||")
    action = input("Do you want to (login/register/forgot password)? ").lower()

    if action == "register":
        register_user()
    elif action == "login":
        if login_with_attempts():
            mainApicall()
    elif action == "forgot password":
        forgot_password()
    else:
        print("❌ Invalid action. Please enter 'login', 'register', or 'forgot password'.")