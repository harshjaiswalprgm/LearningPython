
<<<<<<< HEAD
# Game Price Checker

## Overview
The **Game Price Checker** is a console application that allows users to search for the latest prices of digital PC games from multiple stores using the CheapShark API. The application features user registration, login, password recovery, and the ability to fetch and display game deals.


## Here’s a concise one-line explanation for each library:

import csv: Provides functions to read from and write to CSV (Comma-Separated Values) files for data storage and manipulation.

import bcrypt: Enables secure password hashing and verification to protect user credentials.

import re: Facilitates regular expression operations for string matching and validation, such as email and password checks.

import requests: Simplifies making HTTP requests to APIs and handling responses in Python.

import certifi: Supplies a set of trusted root certificates for validating SSL certificates during HTTPS requests.

import time: Offers various time-related functions for measuring execution time or adding delays in your program.

from prettytable import PrettyTable: Allows for easy creation of ASCII tables for displaying tabular data in a visually appealing format in the console.

## Features
- User registration with email and password
- Secure password hashing for user credentials
- User login with limited attempts
- Password recovery through security questions
- Fetching game deals from the CheapShark API
- Searching for game prices by title
- Displaying top game deals in a user-friendly format
- Saving fetched deals to a CSV file

## Technologies Used
- **Python**: Main programming language
- **bcrypt**: For password hashing
- **requests**: To make API calls to CheapShark
- **csv**: To read and write user and game deal data
- **re**: For input validation
- **certifi**: To verify SSL certificates for HTTPS requests

## Getting Started
### Prerequisites
- Python 3.x
- Install the required packages:
  ```bash
  pip install bcrypt requests prettytable certifi
  ```

### Usage
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd game-price-checker
   ```
3. Run the application:
   ```bash
   python main.py
   ```

4. Follow the prompts to register, log in, or recover your password.

## Code Explanation

### Constants
- **MAX_ATTEMPTS**: The maximum number of login attempts allowed.
- **attempts**: A counter for tracking login attempts.
- **BASE_URL**: The base URL for the CheapShark API.

### Password Hashing Functions
- **hash_password(password)**: Takes a plaintext password and returns its hashed version.
- **check_password(stored_password, provided_password)**: Checks if the provided password matches the stored hashed password.

### Input Validation Functions
- **is_valid_email(email)**: Validates the email format using a regular expression.
- **is_valid_password(password)**: Validates the password based on criteria like length, and character types.

### User Management Functions
- **save_user_data_to_csv(...)**: Appends user data to `users.csv`.
- **register_user()**: Prompts the user to register and saves their data.
- **login()**: Allows users to log in by checking their credentials.
- **forgot_password()**: Enables users to reset their password using a security question.

### API Interaction Functions
- **get_deals(store_id=1, upper_price=15)**: Fetches game deals from the CheapShark API.
- **save_deals_to_csv(deals)**: Saves fetched game deals to `game_deals.csv`.
- **display_deals(deals)**: Displays the top game deals in a formatted manner.
- **search_game_by_title(game_title)**: Searches for game deals based on the provided title.

### Main Application Logic
- **mainApicall()**: Handles user interactions, including searching for game prices, displaying top deals, and saving deals to a file.
- **if __name__ == "__main__":**: The entry point of the application, which presents the user with options to register, log in, or recover their password.

## Conclusion
The Game Price Checker is a simple yet effective tool for gamers looking to find the best prices for their favorite digital games. Feel free to contribute or improve the application by adding new features or fixing issues!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to update the repository URL and license section as necessary.
=======
>>>>>>> 127066954d12165edd5209977ee57a49e12abb41
--------------------------------------------------------------------------------------------------------------------------------------------------------
Name: Harsh Jaiswal
Reg. No: 12320507
Group: B
All screenshoots related my project
--------------------------------------------------------------------------------------------------------------------------------------------------------


![image](https://github.com/user-attachments/assets/875ebbca-983b-4749-a524-bea8f8a19bb7)





 

 


 
 

