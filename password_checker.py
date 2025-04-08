import re

def password_strength(password: str) -> str:
    """
    Function to check the strength of a given password.
    :param password: Password to be checked
    :return: A string indicating the strength of the password
    """
    
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        return "Password too short! Minimum length is 8 characters."
    
    # Check for the presence of at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase letter."
    
    # Check for the presence of at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password should contain at least one uppercase letter."
    
    # Check for the presence of at least one digit
    if not re.search(r'\d', password):
        return "Password should contain at least one digit."
    
    # Check for the presence of at least one special character
    if not re.search(r'[@$!%*?&]', password):
        return "Password should contain at least one special character."
    
    # If the password passes all the checks
    return "Password is strong!"

def main():
    # User input for password
    password = input("Enter your password: ")
    
    # Check the strength of the entered password
    result = password_strength(password)
  
    print(result)

if __name__ == "__main__":
    main()
