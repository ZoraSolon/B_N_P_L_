#onboarding.py
#created by ZoraSolon
#This is the onboarding/ account creation process

"""
def create_user():
    
    Flow for Onboarding, Compliance, & Analytics:
    
    1. Validate the intake form:
       - Check that all required fields are filled out and correctly formatted.
       - If anything is missing or invalid -> stop and return an error.
       
    2. Check for duplicate accounts:
       - Look up email and SSN in the 'users' database table.
       - If user already exists -> load their existing user_id instead of duplicating.

    3. Run identity & compliance checks (CIP / KYC / OFAC screening):
         - Package customer data (Name, SSN, DOB, Address).
         - Make an API call to the compliance/issuer provider 
           which evaluates the applicant against the Sponsor Bank's approved CIP/OFAC rules.
         - Receive response:
             * If "APPROVED" -> proceed to debit card linking.
             * If "DECLINED" or "OFAC_HIT" -> immediately halt onboarding, log the exact 
               regulatory decline reason in the database, and return a clean rejection response.

    4.  Return the unique user_id so they can proceed to bank linking and preapproval
        4a link bank account(s) through plaid
        4b underwitiring.py verified income based approval

    5. Prompt user to link a repayment debit card:
       - Collect card details / token.
       - Check card expiration date: if it expires this month -> block 
         onboarding and ask the user to provide a valid, unexpired card.

    6. Save verified user profile & card token to the database:
       - Securely save structured profile fields into the 'users' table.
       - Associate the verified debit card token with the user profile.

    7. Start an analytics session (for window-shopping / funnel tracking):
       - Log a new event in the 'loan_requests' table tied to this user_id 
         with status = "onboarding_completed" (so you can track if they drop off later).
    
    # TODO: Step 1 - Validate form fields
    # TODO: Step 2 - Check duplicate user lookup
    # TODO: Step 3 - Execute CIP/KYC/OFAC API check
    # TODO: Step 4 - Validate debit card expiration window
    # TODO: Step 5 - Save user and card token to database
    # TODO: Step 6 - Log funnel/session status for window-shopping analytics
    # TODO: Step 7 - Return user_id
    pass
"""  


def create_user():
    print("=== Let's get to know you ===\n")

    # Collect inputs directly into a dictionary
    user_data = {
        "first_name": input("Enter your first name: "),
        "middle_name": input("Enter your middle name (press Enter if none): "),
        "last_name": input("Enter your last name: "),
        "suffix": input("Enter your suffix (e.g., Jr., III, press Enter if none): "),
        "ssn": input("Enter your SSN (9 digits): "),
        "dob": input("Enter your Date of Birth (YYYY-MM-DD): "),
        "street_address": input("Enter your street address: "),
        "city": input("Enter your city: "),
        "state": input("Enter your state (2 letters): "),
        "zip_code": input("Enter your ZIP code: "),
        "email": input("Enter your email address: "),
        "phone": input("Enter your phone number (10 digits): "),
        "employment_status": input("Enter your employment status (employed, self_employed, etc.): ")
    }
    
    print("\nAccount successfully created!")
    return user_data

def user_login():
    print("Welcome back! Please enter your credentials to log in.")
 
def get_user_data():
    print("=== Let's get to know you ===\n")
    
    # 1. Store your input prompts inside a dictionary
    user_data = {
        "first_name": input("First Name: ").strip(),
        "middle_name": input("Middle Name (press Enter if none): ").strip() or None,
        "last_name": input("Last Name: ").strip(),
        "suffix": input("Suffix (e.g., Jr., III, press Enter if none): ").strip() or None,
        "ssn": input("SSN (9 digits, numbers only): ").strip(),
        "dob": input("Date of Birth (YYYY-MM-DD): ").strip(),
        "street_address": input("Street Address: ").strip(),
        "city": input("City: ").strip(),
        "state": input("State (2 letters): ").strip().upper(),
        "zip_code": input("ZIP Code: ").strip(),
        "email": input("Email Address: ").strip(),
        "phone": input("Phone Number (10 digits): ").strip(),
        "employment_status": input("Employment Status (employed, self_employed, retired, unemployed): ").strip().lower()
    }
    
    # 2. Return the dictionary so the main program can use it
    return user_data

# --- Main Program Flow ---
print("Hello, Welcome to Zora! \nThis is a wonderful place to be, let's see how we can help you. \nPlease follow the prompts.\n")

is_new_user = True  # Or gathered from an input/check

if is_new_user:
    # 1. Call the function and store the returned dictionary
    created_user_data = create_user()
    
    # 2. Extract the first_name from the dictionary
    first_name = created_user_data["first_name"]

else:
    user_login()


# Print out success message and move on to next step
print(f"\n--- Great {first_name}! ---")
print("Now link your bank account via Plaid to get your buying power")